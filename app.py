import datetime as dt
from steemdata import SteemData
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin 

app = Flask(__name__)
CORS(app)

s = SteemData()
time_constraints = {
    '$gte': dt.datetime.now() - dt.timedelta(days=7)}

#GET "TO" Transfer
@app.route('/to/<string:toexch>')
def to_exchange(toexch):

    to_result = list(s.Operations.find({'type': 'transfer', 'to': toexch, 'timestamp': time_constraints},
        sort=[('timestamp', -1)],
        projection={"_id": 0, "amount.amount": 1, "timestamp": 1, "amount.asset": 1, "from": 1, "to": 1}))

    return jsonify({'to_result': to_result})

#GET "FROM"  Transfer
@app.route('/from/<string:fromexch>')
def from_exchange(fromexch):

    from_result = list(s.Operations.find({'type': 'transfer', 'from': fromexch, 'timestamp': time_constraints},
         sort=[('timestamp', -1)],
        projection={"_id": 0, "amount.amount": 1, "timestamp": 1, "amount.asset": 1, "from": 1, "to": 1}))

    return jsonify({'from_result': from_result})

if __name__ == '__main__':
   app.run(debug=True)
