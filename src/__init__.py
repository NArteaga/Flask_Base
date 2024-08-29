
from flask import Flask
from src.libs.alchemy_db import SQLAlchemyClient

router = Flask(__name__)

client = SQLAlchemyClient()
from src.app import *

client.create_table()