from page import app

if __name__ == '__main__':
    app.config['FLASK_ENV'] = 'development'
    app.run('localhost', 5000)