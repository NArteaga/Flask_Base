import os, time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from sqlalchemy.engine import url

class SQLAlchemyClient:
  def __init__(self):
    db_url = url.URL.create(
      drivername = os.environ["SQL_ALCHEMY_DRIVER"],
      username = os.environ["SQL_ALCHEMY_USER"],
      password = os.environ["SQL_ALCHEMY_PASSWORD"],
      database = os.environ["SQL_ALCHEMY_DATABASE"],
      host = os.environ["SQL_ALCHEMY_HOST"],
      port = os.environ["SQL_ALCHEMY_PORT"],
    )

    self.engine = create_engine(db_url)
    self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
    self.mapper_registry = registry()
  
  def create_table(self):
    connection_tries = 1
    while connection_tries < 3:
      try:
        self.mapper_registry.metadata.create_all(self.engine)
        break
      except Exception as e:
        print(e)
        connection_tries += 1
        time.sleep(5)