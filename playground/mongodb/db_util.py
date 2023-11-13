import motor.motor_asyncio
import asyncio
from datetime import datetime
from datetime import timedelta 
import pprint


client = motor.motor_asyncio.AsyncIOMotorClient()

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://abhi:abhi@cluster0.17p1u0e.mongodb.net/')

db = client.lmsdb
collection = db.students
current_date: datetime = datetime.today()

async def do_insert(document):
    document = document
    result = await collection.insert_one(document)
    print('result %s' % repr(result.inserted_id))

async def do_find_one(studentId):
    document = await collection.find_one({'studentId': studentId})
    pprint.pprint(document)


async def do_replace(studentId,updated_student_doc):
    old_document = await collection.find_one({'studentId': studentId})
    print('found document: %s' % pprint.pformat(old_document))
    _id = old_document['_id']
    result = await collection.replace_one({'_id': _id}, updated_student_doc)
    print('replaced %s document' % result.modified_count)
    new_document = await collection.find_one({'_id': _id})
    print('document is now %s' % pprint.pformat(new_document))


def insert_student(document):
    loop = client.get_io_loop()
    loop.run_until_complete(do_insert(document))

def fetch_student(studentId):
    loop = client.get_io_loop()
    loop.run_until_complete(do_find_one(studentId))

def update_student(studentId,updated_student_doc):
    loop = client.get_io_loop()
    loop.run_until_complete(do_replace(studentId,updated_student_doc))



if __name__ == "__main__":
    student_doc = {
                "studentId": 1,
                "fullName": "John Doe",
                "ofClass": 5,
                "books": [
                    {
                    "name": "The Adventures of Huckleberry Finn",
                    "author": "Mark Twain",
                    "issueDate": current_date,
                    "issuedUntilDate":current_date + timedelta(days=30)
                    },
                ]
                }
    
    updated_student_doc = {
            "studentId": 2,
            "fullName": "Jennie Dsouza",
            "ofClass": 5,
            "books": [
                {
                "name": "Wuthering Heights",
                "author": "Emily Bronte",
                "issueDate": current_date - timedelta(days=5),
                "issuedUntilDate":current_date + timedelta(days=30)
                }
            ]
            }
    # insert_student(student_doc)
    update_student(1,student_doc)
    # fetch_student(1)