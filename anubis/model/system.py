from anubis import db
from anubis.util import argmethod


@argmethod.wrap
async def inc_user_counter():
    """Increments the user counter.

    Returns:
        Integer value after increment.
    """
    coll = db.Collection('system')
    doc = await coll.find_one_and_update(filter={'_id': 'user_counter'},
                                         update={'$inc': {'value': 1}},
                                         upsert=True,
                                         return_document=True)
    return doc['value']


@argmethod.wrap
async def create_indexes():
    coll = db.Collection('system')
    await coll.find_one_and_update(filter={'_id': 'user_counter'},
                                   update={'$setOnInsert': {'value': 1}},
                                   upsert=True)


if __name__ == '__main__':
    argmethod.invoke_by_args()