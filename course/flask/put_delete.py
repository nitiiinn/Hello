# This is a file consisiting of basic to do list tasks

from flask import Flask, jsonify,  request
 
app = Flask(__name__)

#initial data
items=[
    {'id':1, 'name':'item1', 'description':'This is item 1'},
    {'id':2, 'name':'item2', 'description':'This is item 2'},
    {'id':3, 'name':'item3', 'description':'This is item 3'}]

@app.route('/')
def welcome():
    return 'Welcome to this page'

#GET : retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET : retrieve specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):  
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify('error: Item not found')

# post : create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'Name is required'})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT : update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):   
    if not request.json:
        return jsonify({'error': 'Request body is required'}), 400
    for item in items:
        if item['id'] == item_id:
            item['name'] = request.json.get('name', item['name'])
            item['description'] = request.json.get('description', item['description'])
            return jsonify(item)
    return jsonify({'error': 'Item not found'})


# DELETE : delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])          
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)