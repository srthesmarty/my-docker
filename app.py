# app.py
from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.todoDB
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    
    if item_name and item_desc:
        collection.insert_one({
            "name": item_name,
            "description": item_desc
        })
        return redirect('/')
    return "Missing Fields", 400

if __name__ == '__main__':
    app.run(debug=True)
