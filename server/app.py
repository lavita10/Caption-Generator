from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
#app = Flask(__name__, static_url_path='')
#app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = r"./upload"
CORS(app) 

# enable CORS
#CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/')

@app.route('/upload',methods=["POST"]) # The method should be consistent with the front end
def upload():
    file_obj = request.files['file']  # Get files in Flask
    print(file_obj)
    if file_obj is None:
        # Indicates that no file was sent
        return "File not uploaded"
    #save document
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")     
    file_obj.save(file_path)
    return file_path
    
if __name__ == '__main__':
    app.run()