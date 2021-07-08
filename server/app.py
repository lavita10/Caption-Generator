from flask import Flask, jsonify, request, render_template, url_for
from flask_cors import CORS
import os
import json
#from .helperFunction import getCaption
import helperFunction
import datetime

# configuration
DEBUG = True

# instantiate the app
#app = Flask(__name__)
app = Flask(__name__, static_url_path='')


#app = Flask(__name__, static_url_path='')
#app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = r"./static"
CORS(app) 

DOMAIN_NAME = 'http://127.0.0.1:5000/'

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
    response_obj = {
        'message' : 'An error occured'
    }
    if file_obj is None:
        # Indicates that no file was sent
        response_obj['message'] = "File not found"
        return response_obj
    file_name = ''.join(datetime.datetime.now().strftime("%d%m%Y%f").split()) + ".jpg"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)     
    file_obj.save(file_path)
    #print(file_path)
    #print(url_for("static", filename = "1.jpg"))
    response_obj['image'] = DOMAIN_NAME + file_name
    generated_captions = helperFunction.getCaption(file_name)
    response_obj['caption'] = generated_captions
    #response_obj['caption'] = helperFunction.getCaption(file_obj)
    response_obj['message'] = "Caption successfully generated."
    generated_audio = [helperFunction.generate_audio(audio) for audio in generated_captions]
    for audioFileName, index in enumerate(generated_audio):
        response_obj[f'AudioURL{index}'] = DOMAIN_NAME + f"Audio/{audioFileName}"
    
    return response_obj
    #save document
   
    #return file_path
    
if __name__ == '__main__':
    app.run()