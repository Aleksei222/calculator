from db import db, app
from flask import session, request, make_response
from pyton.correct import correct
from pyton.calc import calc
from hashlib import sha256
from models import User, Token
from datetime import date
import json



# @app.route('/base', methods=['GET'])
# def base():
#     return render_template('base.html')

# @app.route('/', methods=['GET'])
# def main():
#     return render_template('index.html')

@app.route('/api/calc/', methods=['POST'])
def getCalc():
    inp = request.get_json()['expression']
    if correct(inp):            
        value = calc(inp)
    else:
        value = 'incorrect'
    return json.dumps({'value': value})
    
@app.route('/api/login/', methods=['POST', 'GET'])
def getLogin():
    if request.method == 'POST':
        inp = request.get_json()
        login = inp['login']
        password = inp['password']
        user = User.query.filter_by(login=f"{login}").first()
        if user:
            if user.password == sha256(bytes(password, 'utf8')).hexdigest():
                status = 200
                token = sha256(bytes(str(user.login), 'utf8')).hexdigest()
                body = token 
                token = Token(token, user.id, str(date.today()))
                db.session.add(token)
                db.session.commit()
            else:
                status = 403
        else:
            status = 403
        return json.dumps({'status': status, 'cookie': f'token={body}; max-age=3600*24*365; secure=true'})
    elif request.method == 'GET':
        print(request.cookies.get('token'))
        return make_response()
# @app.route('/api/test/', methods=['GET'])
# def cokie():
#     res = make_response()
#     res.set_cookie('token', 'test')
#     return res

# @app.route('/api/gettest/', methods=['GET'])
# def getCokie():
#     res = make_response()
#     print(request.cookies)
#     return res