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

*We learnt the basics of API development and basics of FastAPI yesterday. While there is so much deep dive still about to happen, let's complete the basic building blocks first.*

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