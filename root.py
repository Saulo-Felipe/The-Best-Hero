import os
from database import connect

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
connection = connect.connection
