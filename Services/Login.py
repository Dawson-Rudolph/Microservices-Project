from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = json.loads(request.data)
    if user['username'] == 'TopicsInSE' and user['password'] == 'CS480':
        return jsonify({'message': 'Correct username & password. You are now logged in.'}), 200
    else:
        return jsonify({'message': 'Incorrect username or password. Please try again.'}), 400


@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({'messsage': 'You are now logged out.'}), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
