from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.User)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_Users', methods = ['GET'])
def create_Users():
    db_session = db.getSession(engine)
    usuarios = entities.User(Codigo=201810642, Nombre="Mauricio", Apellido="Rodriguez", Password="Utec5141")
    db_session.add(usuarios)
    db_session.commit()
    return "Test user created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded = True, host=('0.0.0.0'))
