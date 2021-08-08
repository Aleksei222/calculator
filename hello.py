from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pyton.correct import correct
from pyton.calc import calc

app = Flask("compute")
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aheling23'
app.config['MYSQL_DATABASE_DB'] = 'calcul'
app.config['MYSQL_DATABASE_PORT'] = '5000'
mysql.init_app(app)



@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        value = ""
        return render_template('index.html', value = value)
    if request.method == 'POST':
        inp = request.form['input']
        if correct(inp):            
            value = calc(inp)
        else:
            value = "incorrect"     
    return render_template('index.html', value = value)
    
if __name__ == "__main__":
    app.run()