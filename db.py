from hello import app
from flask_sqlalchemy import SQLAlchemy


username = 'root'
password = 'Aheling23.'
host = 'localhost'
port = 3306 
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/calc"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
