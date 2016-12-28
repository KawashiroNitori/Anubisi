import collections
import datetime

from anubis.util import version
from anubis import constant

# Permissions.
PERM_NONE = 0

# Domain settings.
PERM_VIEW = 1 << 0
PERM_EDIT_PERM = 1 << 1
PERM_MOD_BADGE = 1 << 2
PERM_EDIT_DESCRIPTION = 1 << 3


# Problem and Record.
PERM_CREATE_PROBLEM = 1 << 4
PERM_EDIT_PROBLEM = 1 << 5
PERM_EDIT_PROBLEM_SELF = 1 << 6
PERM_VIEW_PROBLEM = 1 << 7
PERM_VIEW_PROBLEM_HIDDEN = 1 << 8
PERM_SUBMIT_PROBLEM = 1 << 9
PERM_READ_PROBLEM_DATA = 1 << 10
PERM_READ_PROBLEM_DATA_SELF = 1 << 11
PERM_READ_RECORD_CODE = 1 << 12
PERM_READ_RECORD_DETAIL = 1 << 13
PERM_REJUDGE_PROBLEM = 1 << 14
PERM_REJUDGE = 1 << 15

# Discussion.
PERM_VIEW_DISCUSSION = 1 << 27
PERM_CREATE_DISCUSSION = 1 << 28
PERM_HIGHLIGHT_DISCUSSION = 1 << 29
PERM_EDIT_DISCUSSION = 1 << 30
PERM_EDIT_DISCUSSION_SELF = 1 << 31
PERM_DELETE_DISCUSSION = 1 << 32
PERM_DELETE_DISCUSSION_SELF = 1 << 33
PERM_REPLY_DISCUSSION = 1 << 34
PERM_EDIT_DISCUSSION_REPLY = 1 << 35
PERM_EDIT_DISCUSSION_REPLY_SELF = 1 << 36
PERM_EDIT_DISCUSSION_REPLY_SELF_DISCUSSION = 1 << 37
PERM_DELETE_DISCUSSION_REPLY = 1 << 38
PERM_DELETE_DISCUSSION_REPLY_SELF = 1 << 39
PERM_DELETE_DISCUSSION_REPLY_SELF_DISCUSSION = 1 << 40

# Contest
PERM_VIEW_CONTEST = 1 << 41
PERM_VIEW_CONTEST_STATUS = 1 << 42
PERM_VIEW_CONTEST_HIDDEN_STATUS = 1 << 43
PERM_CREATE_CONTEST = 1 << 44
PERM_ATTEND_CONTEST = 1 << 45

# Training.
PERM_VIEW_TRAINING = 1 << 46

PERM_ALL = -1

PERM_TEXTS = collections.OrderedDict([
    (PERM_VIEW, 'View this domain'),
    (PERM_EDIT_PERM, 'Edit permission of a role'),
    (PERM_MOD_BADGE, 'Show MOD Badge'),
    (PERM_EDIT_DESCRIPTION, 'Edit description of this domain'),
    (PERM_CREATE_PROBLEM, 'Create problems'),
    (PERM_EDIT_PROBLEM, 'Edit problems'),
    (PERM_EDIT_PROBLEM_SELF, 'Edit own problems'),
    (PERM_VIEW_PROBLEM, 'View problems'),
    (PERM_SUBMIT_PROBLEM, 'Submit problem'),
    (PERM_READ_PROBLEM_DATA, 'Read data of problem'),
    (PERM_READ_PROBLEM_DATA_SELF, 'Read data of own problems'),
    (PERM_READ_RECORD_CODE, 'Read record codes'),
    (PERM_READ_RECORD_DETAIL, 'Read record details'),
    (PERM_REJUDGE_PROBLEM, 'Rejudge problems'),
    (PERM_REJUDGE, 'Rejudge records'),
    (PERM_VIEW_DISCUSSION, 'View discussions'),
    (PERM_CREATE_DISCUSSION, 'Create discussions'),
    (PERM_HIGHLIGHT_DISCUSSION, 'Highlight discussions'),
    (PERM_EDIT_DISCUSSION, 'Edit discussions'),
    (PERM_EDIT_DISCUSSION_SELF, 'Edit own discussions'),
    (PERM_DELETE_DISCUSSION, 'Delete discussions'),
    (PERM_DELETE_DISCUSSION_SELF, 'Delete own discussions'),
    (PERM_REPLY_DISCUSSION, 'Reply discussions'),
    (PERM_EDIT_DISCUSSION_REPLY, 'Edit discussion replies'),
    (PERM_EDIT_DISCUSSION_REPLY_SELF, 'Edit own discussion replies'),
    (PERM_EDIT_DISCUSSION_REPLY_SELF_DISCUSSION, 'Edit discussion replies of own discussion'),
    (PERM_DELETE_DISCUSSION_REPLY, 'Delete discussion replies'),
    (PERM_DELETE_DISCUSSION_REPLY_SELF, 'Delete own discussion replies'),
    (PERM_DELETE_DISCUSSION_REPLY_SELF_DISCUSSION, 'Delete discussion replies of own discussion'),
    (PERM_VIEW_CONTEST, 'View contests'),
    (PERM_VIEW_CONTEST_STATUS, 'View contest status'),
    (PERM_VIEW_CONTEST_HIDDEN_STATUS, 'View hidden contest status'),
    (PERM_CREATE_CONTEST, 'Create contests'),
    (PERM_ATTEND_CONTEST, 'Attend contests'),
    (PERM_VIEW_TRAINING, 'View training'),
    (PERM_ALL, 'Have ALL PERMISSIONS in this domain')
])

# Privileges.
PRIV_NONE = 0
PRIV_SET_PRIV = 1 << 0
PRIV_SET_PERM = 1 << 1
PRIV_USER_PROFILE = 1 << 2
PRIV_REGISTER_USER = 1 << 3
PRIV_READ_PROBLEM_DATA = 1 << 4
PRIV_READ_PRETEST_DATA = 1 << 5
PRIV_READ_PRETEST_DATA_SELF = 1 << 6
PRIV_READ_RECORD_CODE = 1 << 7
PRIV_READ_RECORD_DETAIL = 1 << 8
PRIV_VIEW_HIDDEN_RECORD = 1 << 9
PRIV_WRITE_RECORD = 1 << 10
PRIV_CREATE_DOMAIN = 1 << 11
PRIV_VIEW_ALL_DOMAIN = 1 << 12
PRIV_MANAGE_ALL_DOMAIN = 1 << 13
PRIV_REJUDGE = 1 << 13
PRIV_ALL = -1

DEFAULT_PRIV = PRIV_USER_PROFILE | PRIV_CREATE_DOMAIN

# Roles.
ROLE_GUEST = 'guest'
ROLE_DEFAULT = 'default'
ROLE_ADMIN = 'admin'

# Domains.
DOMAIN_ID_SYSTEM = 'system'
BASIC_PERMISSIONS = (
    PERM_VIEW |
    PERM_VIEW_DISCUSSION |
    PERM_VIEW_CONTEST |
    PERM_VIEW_CONTEST_STATUS
)
DEFAULT_PERMISSIONS = (
    PERM_VIEW |
    PERM_VIEW_PROBLEM |
    PERM_EDIT_PROBLEM_SELF |
    PERM_SUBMIT_PROBLEM |
    PERM_READ_PROBLEM_DATA_SELF |
    PERM_VIEW_DISCUSSION |
    PERM_CREATE_DISCUSSION |
    PERM_REPLY_DISCUSSION |
    PERM_VIEW_CONTEST |
    PERM_VIEW_CONTEST_STATUS |
    PERM_VIEW_TRAINING |
    PERM_ATTEND_CONTEST
)
ADMIN_PERMISSIONS = PERM_ALL
DOMAIN_SYSTEM = {
    '_id': DOMAIN_ID_SYSTEM,
    'owner_uid': 0,
    'roles':{
        ROLE_GUEST: BASIC_PERMISSIONS,
        ROLE_DEFAULT: DEFAULT_PERMISSIONS,
        ROLE_ADMIN: ADMIN_PERMISSIONS
    },
    'gravatar': '',
    'name': 'Anubis'
}

DOMAINS = [DOMAIN_SYSTEM]

# Users.
UID_SYSTEM = 0
UNAME_SYSTEM = 'Anubis'
USER_SYSTEM = {
    '_id': UID_SYSTEM,
    'uname': UNAME_SYSTEM,
    'uname_lower': UNAME_SYSTEM.strip().lower(),
    'mail': '',
    'mail_lower': '',
    'salt': '',
    'hash': 'anubis|',
    'gender': constant.model.USER_GENDER_OTHER,
    'reg_at': datetime.datetime.utcfromtimestamp(0),
    'reg_ip': '',
    'priv': PRIV_NONE,
    'login_at': datetime.datetime.utcnow(),
    'login_ip': '',
    'gravatar': '',
    'role': ROLE_GUEST
    'num_submit': 0,
    'num_accepted': 0
}
UID_GUEST = 1
UNAME_GUEST = 'Guest'
USER_GUEST = {
    '_id': UID_GUEST,
    'uname': UNAME_GUEST,
    'uname_lower': UNAME_GUEST.strip().lower(),
    'mail': '',
    'mail_lower': '',
    'salt': '',
    'hash': 'anubis|',
    'gender': constant.model.USER_GENDER_OTHER,
    'reg_at': datetime.datetime.utcfromtimestamp(0),
    'reg_ip': '',
    'priv': PRIV_REGISTER_USER,
    'login_at': datetime.datetime.utcnow(),
    'login_ip': '',
    'gravatar': '',
    'role': ROLE_GUEST,
    'num_submit': 0,
    'num_accept': 0
}

USERS = [USER_SYSTEM, USER_GUEST]

FOOTER_EXTRA_HTML = ['Copyright 2010 - 2017 <a href="http://acm.sut.edu.cn">ACM Laboratory DevTeam of SUT</a>',
                     version.get()]