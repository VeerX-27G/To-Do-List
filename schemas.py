# BaseModel is Pydantic's base class used to define data validation "schemas"
# These are NOT database tables — they define the shape of data going in/out of the API.
from pydantic import BaseModel

# Schema used when a client CREATES a new todo (i.e. the request body for POST/PUT).
# FastAPI will validate incoming JSON against this shape automatically.
class TodoCreate(BaseModel):
    title: str                 # title is required and must be a string
    completed: bool = False    # completed is optional; defaults to False if not provided

# Schema used when the API SENDS a todo back to the client (the response body).
# It inherits everything from TodoCreate (title, completed) and adds an id field,
# since a todo only has an id after it's been saved to the database.
class TodoResponse(TodoCreate):
    id: int  # the database-assigned primary key

    # Special inner config class that tells Pydantic:
    # "it's okay to build this schema from an ORM object's attributes"
    # (e.g. reading todo.id, todo.title directly from a SQLAlchemy model instance,
    # not just from a dict). Needed to convert models.Todo -> schemas.TodoResponse.
    class Config:
        from_attributes = True