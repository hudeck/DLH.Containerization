from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = [
    {"id": 1, "name": "Item One", "description": "This is item one"},
    {"id": 2, "name": "Item Two", "description": "This is item two"},
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    if not new_item.get('name') or not new_item.get('description'):
        return jsonify({"error": "Missing name or description"}), 400
    new_item['id'] = items[-1]['id'] + 1 if items else 1
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item.update(updated_data)
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
