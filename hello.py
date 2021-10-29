from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = ' xpressdawa'
app.config['MONGO_URI'] = 'mongodb+srv://dev:664710@cluster0.qndd2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

# client = pymongo.MongoClient("mongodb+srv://dev:664710@cluster0.qndd2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

mongo = PyMongo(app)

@app.route('/framework', methods=['GET'])
def get_a_medicine():
    return 'Hello World!'
    framework = mongo.db.framework 

    output = []
    i=20
    for q in framework.find():
        print(q)
        output.append('sahil')
        output.append({'BrandName' : q['BrandName'], 'Manufratured By' : q['Manufratured By']})
        i-=1
        if(i==0):break;

    # print(framework.find().limit(2))
    # print('sahil')
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)