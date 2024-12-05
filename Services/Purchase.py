from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)

@app.route('/purchase', methods=['POST'])
def purchase():
    purchaseData = json.loads(request.data)
    items = purchaseData['items']
    totalCost = purchaseData['totalCost']
    orderName = purchaseData['orderName']

    if len(purchaseData['creditCardNumber']) != 16:
        return jsonify({'messsage': 'Please provide a valid credit card number.'}), 400
    else:
        return jsonify({'messsage': f'Thank you {orderName} for ordering: {items}. Your total is: ${totalCost}'}), 200

@app.route('/orderUpdate', methods=['POST'])
def orderUpdate():
    deliveryTime = random.randint(0,5)
    if deliveryTime == 0:
        return jsonify({'messsage': 'Your package will be delivered today.'}), 200
    else:
        return jsonify({'message': f'Your package will be delivered in {deliveryTime} days.'}), 200

@app.route('/delivered', methods=['POST'])
def delivered():
    purchaseData = json.loads(request.data)
    location = purchaseData['deliveryLocation']

    return jsonify({'messsage': f'Your package has been delivered to {location}.'}), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)