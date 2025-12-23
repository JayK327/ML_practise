# Put and Delete :HTTP verbs
# Working with JSON APis

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {'id': 1, 'title': 'Buy groceries', 'Description': "This is my grocery list"},
    {'id': 2, 'title': 'Read a book', 'Description': "This is my book which i have to read"}
]

@app.route('/')
def welcome():
    return "Welcome to the Sample TO DO list app"

#GET: retrieve all items
@app.route('/items')
def get_items():
    return jsonify(items)

#GET: retrieve a specific item by id
@app.route('/items/<int:item_id>')
def get_item_by_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Item not found'}), 400
    new_items={
        'id': items[-1]['id']+1 if items else 1,
        'title':request.json['title'],
        'Description':request.json['Description']
    }
    items.append(new_items)
    return jsonify(new_items)


#PUT: update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id ), None)
    if not item:
        return jsonify({'message':'Item not found'}),404
    item['title']=request.get_json().get('title',item['title'])
    item['Description']=request.get_json().get('Description',item['Description'])
    return jsonify(item)

#DELETE: delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({'message':'Item deleted successfully'})

if __name__=="__main__":
    app.run(debug=True)