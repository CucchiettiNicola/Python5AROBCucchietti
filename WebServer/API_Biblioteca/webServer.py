import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Biblioteca online</h1><p>Prototipo di web API.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():

    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    
    return jsonify(cursor.execute(f"""
    SELECT * 
    FROM Books;
    """))

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():

    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    
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

    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    
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

@app.route('/api/v1/resouces/books/add', methods=['GET'])
def api_add():
    sqliteConnection = sqlite3.connect('dbBooks.db')
    cursor = sqliteConnection.cursor()
    
    if 'id' in request.args and 'title' in request.args and 'autor' in request.args and 'published' in request.args:
        id = int(request.args['id'])
        title = request.args['title']
        autor = request.args['autor']
        try:
            published = bool(request.args['published'])
        except:
            return "Error: published not boolean"
        cursor.execute(f"""
            INSERT INTO libri
            VALUES ({id},{title},{autor},{published});
        """)
    else:
        return "Error: No title field provided. Please specify a title, id, autor and published."
    

if __name__== "__main__":
    app.run()