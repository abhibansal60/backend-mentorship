# Welcome to Backend Memtorship by [Shrey Batra](https://www.linkedin.com/in/shreybatra/) November Cohort

**I will be using this repo as a working directory for evrything I learn as apart of the program**

## Task 1

Starting with very basics, we will start with API Development... Learn the basics of Python as we will be following that. Feel free to select your own language, but try to stay on the same boat as everyone for doubt solving. I'll be solving doubts commonly in Python / FastAPI only..

- [x] Start learning FastAPI - https://fastapi.tiangolo.com/
  - The document speaks out loud that FAST API is FAST!!
  - Easy to use
  - Short, means less redundancy
  - Standard Based : This one is very cool, I have added more stuff about this in the next point i.e. *Features*
- [x] 2 min read of features (we are going to use Async Python and gonna beat Go performance) - https://fastapi.tiangolo.com/features/
  - Fast API is based on [Open API](https://github.com/OAI/OpenAPI-Specification) Standards.
  - Automatic docs using [Swagger UI](https://github.com/swagger-api/swagger-ui) and [ReDoc](https://github.com/Rebilly/ReDoc) UI, I had no idea about the latter before today.
  - Based on Modern Python
    - I learned about [Python Type hints ](https://fastapi.tiangolo.com/python-types/)
    - I also read and learn about [Pydantic models](https://fastapi.tiangolo.com/python-types/#pydantic-models) 
    - Here is an [example on pydantics](playground/pydantic_example.py)
- [x] Refresher on Concurrency and Async Await (very noob to pro) - https://fastapi.tiangolo.com/async/
  - I just pray that all documentations are writtent the way this is written
  - Crystal clear explanations and intutive examples
- [x] What are Python Type Hints - https://fastapi.tiangolo.com/python-types/
  - I read this section as a part of the features(second bullet)
  - Created a simple [example here](playground/type_hints.py)
- [x] Complete the First Steps under Tutorial to build a Hello World API - https://fastapi.tiangolo.com/tutorial/
  - Hoorah!! Day1 completed succesfully, recap of the First Steps tutorial
    - Here is [an example](playground/first_steps/main.py) i created folllowing the doc, and the details are below
    - Import FastAPI.
    - Create an app instance.
    - Write a path operation decorator (like @app.get("/")).
    - Write a path operation function (like def root(): ... above).
    - Run the development server (like uvicorn main:app --reload).

## Task 2

*We learned the basics of API development and basics of FastAPI yesterday. While there is so much deep dive still about to happen, let's complete the basic building blocks first.*

Today, being Sunday I guess we can cover more topics...
- [x] Start learning MongoDB - https://www.mongodb.com/docs/manual/introduction/
  - A record in MongoDB is a document, a data structure composed kof key(field) and value pairs
  - MongoDB  Documents are similar to JSON Objects
  - Provide High Performance, High availability, horizontal scalability
- [x] Spin up a FREE FOREVER cluster on MongoDB Atlas (MongoDB Cloud) to learn and test your hands-on exercises - https://www.mongodb.com/docs/manual/tutorial/getting-started/
  - This is an in browser tutorial, hence no installations required
  - I tried to connect to my MongoDB using the VScode following this [tutorial](https://www.mongodb.com/docs/mongodb-vscode/connect/)
    - I was uanble to connect to my db because of authentication issue
    - To resolve that I have to enable DB access from my IP address or rom anywhere under Security settings in MongoDB Cloud dashboard
  - I am able to create a [mongo db playground](playground/mongodb/playground-1.mongodb.js) in VS Code
  - Ran and tested it succesfully
- [x] What are Databases, Collections, Documents? https://www.mongodb.com/docs/manual/core/databases-and-collections/
    IMP: Do not learn about Views, Capped Collections and Clustered Collections.
    - Got to know about the BSON Objects and how its different from JSON
    -Learnt about the Unique identifiers for collections in a DB based on uuid
- [x] Basic CRUD operations - https://www.mongodb.com/docs/manual/crud/
    - Important to see syntax, and then the examples...
    - Learn about Query Operators (How to use and when to use) - https://www.mongodb.com/docs/manual/reference/operator/query/
      - **CREATE**: two methods to perform insert/create operation in mongodb
        - db.collection.insertOne()
        - db.collection.insertMany()
      - **READ**: query a collection for documents
        - db.collection.find()
        - we can specify filters or criteria for returning specific documents
      - **UPDATE**: following methods are used to update document(s) in a collection:
        - db.collection.updateOne
        - db.collection.updateMany()
        - db.collection.replaceOne()
      - **DELETE**: to remove one or more documents from a collection
        - db.collection.deleteOne()
        - db.collection.deleteMany()

This is just the basics, the tip of the iceberg (5%) of MongoDB. Just learn it native to MongoDB (run commands via MongoDB Shell, directly on MongoDB Atlas or use MongoDB Compass)
We will then start integrating with applications later!



# Task 3

Integration time!! Now that we have learned how to build simple APIs in FastAPI, and basic CRUD in MongoDB, let's connect the two.

- [x] Build a simple library management service --> create, update, delete students --> in FastAPI. Learn how to pass query params, request bodies and URL Params.... Follow the tutorial for help - https://fastapi.tiangolo.com/tutorial/
- [x] The APIs should save, modify and delete the data in the database - Use MongoDB, spin up a free forever M0 cluster on MongoDB Atlas for testing....
- [x] To use MongoDB in Python, we have pymongo as the official driver for Python. But this is a sync driver -- meaning, it will not have the goodness of async/await we learned that FastAPI comes out of the box with!
- [x] To overcome this, MongoDB released their official Async Python driver - motor which is nothing but an async wrapper on PyMongo. So essentially the same functions/syntax, but just using AsyncIOMotorClient rather than MongoClient and also using async/await.....

Help Links
https://pymongo.readthedocs.io/en/stable/
https://motor.readthedocs.io/en/stable/ (Use AsyncIO Tutorial - https://motor.readthedocs.io/en/stable/tutorial-asyncio.html)

### How I approached the problem

1. Went through the [task 2](#task-2) pointers
2. Thought about coming up with 4 unique endpoints initially add,update,view,delete for each of the CRUD operations
   1. But after giving a deeper thought I settled on having 4 endpoints with the same name but different paths or required operation
     - **/health** - GET : A health check endpoint for proving that app is up and running.
     - **/students/** - GET : Returns a JSON list(collection) of all the students in the database
     - **/students/{id}** - GET: Returns a JSON Object(document) if a student exists in collection, with the requested id(in path params) else returns a meaningful response
     - **/students/** - POST : Creates a student document if a valid JSON Request body is supplied with the request and then returns the newly created student document as a result A unique id will be created and provided in the response.
     - **/students/{id}** - PUT: Updates individual fields of an existing student record, Only the provided fields will be updated. Any missing or null fields will be ignored.
     - **/students/{id}** - DELETE: Removes a single student record/document from the database based on the provided id.
3. Code specifics:
   1. [app.py](playground/library-management-service/app.py): Entry point of the application, containing all the endpoint definitions with path operation decorator.
   2. [client.py](playground/library-management-service/client.py): A helper class for the mongodb related operations (CRUD).
   3. [models.py](playground/library-management-service/models.py): Pydantic models for the document objects we require for the student collection in mongodb
      -  StudentModel
      -  UpdateStudentModel
      -  Book



### Learnings/Questions:

- PyMongo doesn't support saving date instances. The server doesn't have a type for dates without times, so there would have to be some convention used to save dates without times. If you need to save a date your client should convert it to a datetime instance, and you can save that.
  - So datetime.date.today() should be replaced with datetime.datetime.today()
- *id resolution problem*: I am just stuck at one point the Id we provide while creating the object say id: "S1", it gets converted to BSON Object ID because we are using ObjectId(id) before and as it gets save to MongoDB something like "6551eb387e7bc34af6695746", But then while searching I still have to search by "6551eb387e7bc34af6695746" and not S1, which is weird, I must be missing the trick here [?]
- We have used [Motor](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html) to use mongodb with asynci in python 
- References from https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/#creating-the-application helped to shape the application

# Task 4
Lets start building complex queries in mongodb...
Learn what are query operators -
https://www.mongodb.com/docs/manual/reference/operator/query/

Today let's learn how to build multiple logics in our Queries...
$eq, $or, $in, $exists, $regex, $elemMatch, $all --> these are some important ones...!

# Task 5
Let's start learning about Aggregations! 🚀 
We will be learning around this for a few days now, the magic starts now! Step by step, lets see what is Aggregations and then start building the most complicated stuff easily! ❤️

This is going to change the way you look at databases and MongoDB now... 😍 

https://www.mongodb.com/docs/manual/aggregation/
https://www.mongodb.com/docs/manual/core/aggregation-pipeline/

For today, Checkout how to use stages like - $match, $project, $sort, $limit, $count.
Spend the most time in $project, understand how to calculate columns/fields on the fly, do operations and so much more!

I'll be posting some questions and queries in sometime for you to work and solve!


# Task 6
Let's continue our journey with MongoDB Aggregations today -- last open day of learning prerequisites before we start with project tomorrow.

Learn these stages -
$group, $lookup, $unwind, $addFields, $count, $bucket

Yes we can't learn and MUG everything but these are basics which you should when to use what so that when required we know what to Google.

You can take the reference of above video and MongoDB documentation.
Don't read any other blogs/articles/youtube. Might be old.

# Project Start

It has been almost 2 weeks into this program and we have covered a of things till now. You should all be familiar with these concepts till now -

- API Development in FastAPI (get, post, put, patch, delete)
- Familiar with async/await programming
- MongoDB as a database - CRUD and Aggregations, along with Motor client.
- Writing complex queries with MongoDB Aggregations (group, bucket, lookup, unwind)

- We are now going to start building projects (on a group level)
- Each group will have 3-4 members (more on members later)
- Each group will be building an E-Commerce backend layer. (Why?)
- E-commerce because it will teach us concepts like - 
- Multiple models and relationships in MongoDB
- Listing, creating, updating.
- Full Text Search capabilities
- Webhooks and integrations with Payment Gateways.
- Async event streams (queues/kafka)
- dockerising and deploying on cloud

## Project Progress

### (22/11/2023)

Setting up the **Team X** 
  1. Teamed up with Anthony, Sidhhartha, Sumukha and had an intro call.
  2. Sumukha(Obsidian) created a server on Discord and added us to the same .

### (23/11/2023)

Team registration completed with Team name as **Team X**.

### (24/11/2023)

#### Task

Yo @everyone lets start building our projects? 
Okay, so we are building an E-commerce application (you can pick a theme -- general, healthcare, fintech, foodtech, etc..) My favourite is PlayStation's PS Store (Every product will be same 😛)

Now, first things first....
   * Let's start with building our data models... for example - Products, Cart, Orders, Users, etc...
   * Let's see how you build the models in Pydantic (pydantic classes) thinking about relationships and nesting...

   * Relationships in MongoDB are not PrimaryKey/ForeignKey.. get help reading about $lookup stage and ObjectId.
   * Data modelling in MongoDB is not a flat, normalised DB, alsooo it is not 100% embeddable. Somewhere in between.
   * Inspiration on Data Modelling concepts - https://www.mongodb.com/blog/post/building-with-patterns-a-summary

   * This is an ⤴️ amazing read about Data modelling concepts, read only about -
   * Attribute Pattern
   * Bucket Pattern
   * Extended Reference
   * Polymorphic
   * Tree

#### Team X Update


      




