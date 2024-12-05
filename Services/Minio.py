from minio import Minio
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# create function
@app.route('/upload', methods=['PUT'])
def upload():
    response = json.loads(request.data)
    client = Minio(response['url'], access_key=response['accessKey'], secret_key=response['secretKey'], secure=False)
    
    if client.bucket_exists(response['bucketName']):
        client.fput_object(response['bucketName'], response['filename'], response['filepath'])
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'message': 'Bucket does not exist'}), 400
    
# read function
@app.route('/list', methods=['GET'])
def list():
    response = json.loads(request.data)
    client = Minio(response['url'], access_key=response['accessKey'], secret_key=response['secretKey'], secure=False)

    if client.bucket_exists(response['bucketName']):
        objects = client.list_objects(response['bucketName'], recursive=True)
        object_names = [obj.object_name for obj in objects]
        return jsonify({'objectNames': object_names}), 200
    else:
        return jsonify({'message': 'Bucket does not exist'}), 400

# update function
@app.route('/update', methods=['PATCH'])
def update():
    response = json.loads(request.data)
    client = Minio(response['url'], access_key=response['accessKey'], secret_key=response['secretKey'], secure=False)

    if client.bucket_exists(response['bucketName']):
        client.remove_object(response['bucketName'], response['filename'])
        client.fput_object(response['bucketName'], response['filename'], response['filepath'])
        return jsonify({'message': 'File successfully updated'}), 200
    else:
        return jsonify({'message': 'Bucket does not exist'}), 400

# delete function
@app.route('/delete', methods=['DELETE'])
def delete():
    response = json.loads(request.data)
    client = Minio(response['url'], access_key=response['accessKey'], secret_key=response['secretKey'], secure=False)

    if client.bucket_exists(response['bucketName']):
        client.remove_object(response['bucketName'], response['filename'])
        return jsonify({'message': 'File successfully deleted'}), 200
    else:
        return jsonify({'message': 'Bucket does not exist'}), 400

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)