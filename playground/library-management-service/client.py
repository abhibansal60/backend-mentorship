import motor.motor_asyncio
import asyncio
from datetime import datetime
from datetime import timedelta 
import pprint
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument


client = motor.motor_asyncio.AsyncIOMotorClient()

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://abhi:abhi@cluster0.17p1u0e.mongodb.net/')

db = client.lmsdb
collection = db.students
current_date: datetime = datetime.today()

async def do_insert(document):
    document = document
    result = await collection.insert_one(document)
    print('result %s' % repr(result.inserted_id))
    return result

async def do_find_one(id):
    document = await collection.find_one({'_id': ObjectId(id)})
    print (ObjectId(id))
    pprint.pprint(document)
    return document

async def do_find_all():
    documents = await collection.find().to_list(1000)
    return documents

async def do_replace(id,updated_student_doc):
    old_document = await collection.find_one({'id': id})
    print('found document: %s' % pprint.pformat(old_document))
    _id = old_document['_id']
    result = await collection.replace_one({'_id': _id}, updated_student_doc)
    print('replaced %s document' % result.modified_count)
    new_document = await collection.find_one({'_id': _id})
    print('document is now %s' % pprint.pformat(new_document))


async def do_find_one_and_update(id, updated_student_doc):
    result= await collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": updated_student_doc},
            return_document=ReturnDocument.AFTER,
        )
    return result


async def do_delete_one(id):
    result = await collection.delete_one({'_id': ObjectId(id)})
    return result



def insert_student(document):
    loop = client.get_io_loop()
    loop.run_until_complete(do_insert(document))

def fetch_student(id):
    loop = client.get_io_loop()
    loop.run_until_complete(do_find_one(id))

def update_student(id,updated_student_doc):
    loop = client.get_io_loop()
    loop.run_until_complete(do_replace(id,updated_student_doc))