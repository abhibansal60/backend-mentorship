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