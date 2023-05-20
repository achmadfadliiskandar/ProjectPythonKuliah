from flask import Flask, request, jsonify
app = Flask(__name__)
stores = [
    {
        'name': 'Toko Bunga',
        'items' : [
            {
                'name' : 'Bunga Kecombrang',
                'price' : 5000
            }
        ]
    },{
        'name' : 'Toko Buku',
        'items' : [
            {
                'name' : 'Buku Tangkuban Perahu',
                'price' : 10000
            }
        ]
    }
]

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores :
        if(store)['name']==name:
            return jsonify(store['name'])
    return jsonify({'message' : 'Store not found'})
   

@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if (store)['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found'})

@app.route('/store',methods = ["POST"])
def create_store():
    req_data = request.get_json()
    new_store = {
        'name': req_data['name'],
        'item' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item',methods=['POST'])
def create_store_item(name):
    for store in stores :
        if(store)['name']==name:
            req_data = request.get_json()
            new_item = {
                'name' : req_data['name'],
                'price' : req_data['price']
            }
        else:
            return 'halaman tidak ada'
        store['item'].append(new_item)
        return jsonify(new_item)

@app.route('/')
def home():
    return "hey"
app.run(debug = True,port=8000)