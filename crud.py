import flask
import json
from flask import request,jsonify
app = flask.Flask(__name__)

# mendapatkan data
@app.route("/api/v1/resources/books/all",methods=['GET'])
def api_all():
    f = open("data.json")
    books = json.load(f)
    return jsonify(books)

# memfilter/searching data
@app.route('/api/v1/resources/books',methods=['GET'])
def api_id():
    f = open("data.json")
    books = json.load(f)

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'error tidak di temukan'
    
    result = []

    for book in books:
        if book['id'] == id:
            result.append(book)
    return jsonify(result)

# menambahkan data
@app.route('api/v1/resource/books/store',methods=['GET'])
def api_store():
    f = open("data.json")
    books = json.load(f)
    if 'id' in request.form:
        id = int(request.form['id'])
    else:
        return 'error tidak di temukan'
    
    for book in books:
        if book['id'] == id:
            return 'error data telah ditambahkan'
    
    data = {
        "id":id,
        "title":request.form['title'],
        "author":request.form['author'],
        "first_sentence":request.form['first_sentence'],
        "year_published":request.form['year']
    }
    books.append(data)

    with open("data.json","w") as file:
        json.dump(books,file)
    return jsonify(data)

# mengubah data
@app.route("/api/v1/resource/books/update",methods=['PUT'])
def api_update():
    f = open("data.json")
    books = json.load(f)

    if 'id' in request.form:
        id = int(request.form['id'])
    else:
        return 'error tidak di temukan'
    
    for i in range(len(books)):
        if books[i]['id'] == id:
                data = {
                    "id":id,
                    "title":request.form['title'],
                    "author":request.form['author'],
                    "first_sentence":request.form['first_sentence'],
                    "year_published":request.form['year']
                }
                books[i] = data
                break
        else:
            return "Warning Id Not Found"


    with open("data.json","w") as file:
        json.dump(books,file)
    return "Data Berhasil Diubah"

# menghapus data
@app.route("/api/v1/resource/books/delete",methods=['DELETE'])
def api_delete():
    f = open("data.json")
    books = json.load(f)
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'error tidak di temukan'
    
    for i in range(len(books)):
        if books[i]["id"] == id:
            del books[i]
            break
        else:
            return "Warning Id Not Found"
        
    with open("data.json","w") as file:
        json.dump(books,file)
    return "Data Berhasil Dihapus"

app.run()