from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pyton.correct import correct
from pyton.calc import calc
import json

app = Flask("compute")
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aheling23'
app.config['MYSQL_DATABASE_DB'] = 'calcul'
app.config['MYSQL_DATABASE_PORT'] = '5000'
mysql.init_app(app)



@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/api/calc/', methods=['POST'])
def get_calc():
    inp = request.get_json()['expression']
    if correct(inp):            
        value = calc(inp)
        placeholder = ''
    else:
        placeholder = "incorrect"
        value = ''
    return json.dumps({"value": value, "placeholder": placeholder})
    
if __name__ == "__main__":
    app.run()