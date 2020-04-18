import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(cursor.execute(f"""
    SELECT * 
    FROM Books;
    """))

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []
    results.append(cursor.execute(f"""
    SELECT id 
    FROM Books
    WHERE id == {id};
    """))
    return jsonify(results)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_title():
    if 'title' in request.args:
        title = request.args
    else:
        return "Error: No title field provided. Please specify a title."
    
    results = []

    results.append(cursor.execute(f"""
    SELECT title 
    FROM Books
    WHERE title == {title};
    """))
    return jsonify(results)

if __name__== "__main__":
    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    app.run()