from fastapi import FastAPI, HTTPException, status, Response
from models import StudentCollection, StudentModel, UpdateStudentModel
import client

app = FastAPI()

@app.get("/health")
async def root():
    return {"message":"LMS App is up and running!"}


@app.get(
    "/students/",
    response_description="List all students",
    response_model=StudentCollection,
    response_model_by_alias=False,
)
async def get_all_students():
    return StudentCollection(students=await client.do_find_all())

@app.get(
    "/students/{id}",
    response_description="Get a single student",
    response_model=StudentModel,
    response_model_by_alias=False,
)
async def show_student(id: str):
    """
    Get the record for a specific student, looked up by `id`.
    """
    if (
        student := await client.do_find_one(id)
    ) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@app.post(
    "/students/",
    response_description="Add new student",
    response_model=StudentModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_student(student: StudentModel):
    """
    Insert a new student record.

    A unique `id` will be created and provided in the response.
    """
    new_student = await client.do_insert(
        student.model_dump(by_alias=True, exclude=["id"])
    )
    created_student = await client.do_find_one(new_student.inserted_id)
    return created_student



@app.put(
    "/students/{id}",
    response_description="Update a student",
    response_model=StudentModel,
    response_model_by_alias=False,
)
async def update_student(id: str, student: UpdateStudentModel):
    """
    Update individual fields of an existing student record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    student = {
        k: v for k, v in student.model_dump(by_alias=True).items() if v is not None
    }

    if len(student) >= 1:
        update_result = await client.do_find_one_and_update(id, student)
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Student {id} not found")

    # The update is empty, but we should still return the matching document:
    if (existing_student := await client.do_find_one(id)) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.delete("/students/{id}", response_description="Delete a student")
async def delete_student(id: str):
    """
    Remove a single student record from the database.
    """
    delete_result = await client.do_delete_one(id)

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")