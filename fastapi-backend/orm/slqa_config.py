from sqlalchemy import create_engine

# create a connection string
connection_string = "postgresql://username:password@hostname:port/database"

# create the engine
engine = create_engine(connection_string)