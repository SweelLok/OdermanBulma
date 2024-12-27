from flask import Flask
from connection import create_table


app = Flask(__name__)
app.config["SECRET_KEY"] = "q"
create_table()
