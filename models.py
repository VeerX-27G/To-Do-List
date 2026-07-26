# Column types we need: Integer for numbers, String for text, Boolean for true/false
from sqlalchemy import Column, Integer, String, Boolean

# Import the Base class we defined in database.py — our table must inherit from it
from database import Base

# Define a "Todo" table by creating a Python class that inherits from Base.
# Each class attribute below becomes a column in the actual SQL table.
class Todo(Base):
    __tablename__ = "todos"  # the actual name of the table in the database

    # Primary key column — unique identifier for each row, auto-incremented by default.
    # index=True creates a database index on this column for faster lookups.
    id = Column(Integer, primary_key=True, index=True)

    # A text column to store the todo's title/description.
    # index=True speeds up searches/filters on this column.
    title = Column(String, index=True)

    # A boolean column to track whether the todo is done.
    # default=False means new rows will be "not completed" unless specified otherwise.
    completed = Column(Boolean, default=False)