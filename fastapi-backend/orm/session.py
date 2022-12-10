from sqlalchemy.orm import sessionmaker
from orm.sqla_config import engine

# Create an engine to connect to the database

# Create a session factory
Session = sessionmaker(
    bind=engine,
    autoflush=True,
    autocommit=False,
    expire_on_commit=True,
    extension=None,
    query_cls=None,
    query_property=None,
    transaction_cls=None,
    transactional=False,
    twophase=False,
    weak_identity_map=False,
)

# Create a new session
session = Session()


def managed_session(db_session: Session):

    try:
        db_session.commit()
    except Exception as ex:
        db_session.rollback()
        raise ex
