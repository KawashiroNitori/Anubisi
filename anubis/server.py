import logging
import asyncio
import logging.config
import os
import sys
import socket
import urllib.parse
import atexit
import signal

from anubis.util import options
from anubis import app

options.define('listen', default='http://localhost:8888', help='Server listening address.')
options.define('prefork', default=0, help='Number of prefork workers')
options.define('log_format',
               default=('%(log_color)s[%(levelname).1s '
                        '%(asctime)s %(module)s:%(lineno)d]%(reset)s %(message)s'), help='Log format.')
_logger = logging.getLogger(__name__)


def main():
    logging.config.dictConfig({
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
        },
        'formatters': {
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': options.options.log_format,
                'datefmt': '%y%m%d %H:%M:%S'
            }
        },
        'root': {
            'level': 'DEBUG' if options.options.debug else 'INFO',
            'handlers': ['console'],
        },
        'disable_existing_loggers': False,
    })
    _logger.info('Server listening on %s', options.options.listen)
    url = urllib.parse.urlparse(options.options.listen)
    if url.scheme is 'http':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        host, port_str = url.netloc.rsplit(':', 1)
        sock.bind((host, int(port_str)))
    elif url.scheme is 'unix':
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            os.remove(url.path)
        except FileNotFoundError:
            pass
        sock.bind(url.path)
    else:
        _logger.error('Invalid listening scheme %s', url.scheme)
        return 1

    for i in range(1, options.options.prefork):
        pid = os.fork()
        if not pid:
            break
        else:
            atexit.register(lambda: os.kill(pid, signal.SIGTERM))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(loop.create_server(app.Application().make_handler(), sock=sock))
    loop.run_forever()

if __name__ == '__main__':
    sys.exit(main())