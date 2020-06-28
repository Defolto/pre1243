# import pymongo
# from flask import Flask, jsonify

# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

# CONNECTION_URL = "mongodb+srv://admin:admin@cluster0-x7ysx.mongodb.net/test?retryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_URL)
# db = client.test
# task_database = client["task"]
# task_list_collection = task_database["task_list"]


# @app.route('/')
# @app.route('/index')
# def main():
#     return jsonify(', '.join([str(item.get('text')) for item in task_list_collection.find()]))

# app.run()

from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

user = {
    "name": "Maks",
    "age": 21
}

@app.route("/")
@app.route("/index")
def main():
    return jsonify(user)

