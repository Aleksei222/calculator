from flask import Flask, render_template, request, jsonify
# from flaskext.mysql import MySQL
# from pyton.correct import correct
# from pyton.calc import calc
# import json
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from hashlib import sha256
# from models import User
# from flask_login import LoginManager


app = Flask('compute')
CORS(app, resources = {r'/api/*': {'origins': 'http://localhost:3000/login'}})


# username = 'root'
# password = 'Aheling23.'
# host = 'localhost'
# port = 3306 
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/calc"
# db = SQLAlchemy(app)

# login_manager = LoginManager(app)

# @app.route('/base', methods=['GET'])
# def base():
#     return render_template('base.html')

# @app.route('/', methods=['GET'])
# def main():
#     return render_template('index.html')

# @app.route('/api/calc/', methods=['POST'])
# def getCalc():
#     inp = request.get_json()['expression']
#     if correct(inp):            
#         value = calc(inp)
#     else:
#         value = 'incorrect'
#     return json.dumps({'value': value})
    
# @app.route('/api/login/', methods=['POST'])
# def getLogin():
#     inp = request.get_json()
#     login = inp['login']
#     password = inp['password']
#     user = db.query.filter_by(username=f"{login}").first()
#     if user:
#         if user[-1] == sha256(bytes(password, 'utf8')).hexdigest():
#             res = {'status': 'ok'}
#         else:
#             res = {
#                 'status': 'error',
#                 'body': 'Invalid password'
#             }
#     else:
#         res = {
#             'status': 'error',
#             'body': 'Invalid login'
#         }
#     return json.dumps(res)


# if __name__ == '__main__':
#     app.run('localhost', 5000)
        