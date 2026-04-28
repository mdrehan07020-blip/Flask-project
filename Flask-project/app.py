from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

# Show frontend page
@app.route('/')
def home():
    return render_template('todo.html')

# Handle form submission
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    data = {
        "itemName": item_name,
        "itemDescription": item_desc
    }

    collection.insert_one(data)

    return jsonify({"message": "Item saved successfully"})

if __name__ == '__main__':
    app.run(debug=True)