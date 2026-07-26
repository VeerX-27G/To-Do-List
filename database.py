# Import the function that creates a connection to the database engine
from sqlalchemy import create_engine

# sessionmaker: factory for creating DB "sessions" (a session = a conversation with the DB)
# declarative_base: base class that our ORM models (tables) will inherit from
from sqlalchemy.orm import sessionmaker, declarative_base

# The connection string for our database.
# "sqlite:///./todos.db" means: use SQLite, and store the DB file as todos.db
# in the current directory (relative path, hence the three slashes + dot).
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Create the actual database engine — this is the low-level object
# that manages the connection pool and talks to the DB.
# connect_args={"check_same_thread": False} is SQLite-specific:
# by default SQLite only allows one thread to use a connection,
# but FastAPI can handle requests in multiple threads, so we disable that check.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is a factory (class) we'll call to create new DB sessions.
# autocommit=False -> we must explicitly call commit() to save changes
# autoflush=False  -> SQLAlchemy won't automatically flush pending changes before every query
# bind=engine      -> tells the session which engine/database to use
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the parent class that all our ORM model classes (tables) will extend.
# SQLAlchemy uses this to keep track of all table definitions.
Base = declarative_base()