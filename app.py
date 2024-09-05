import flask
import os


#Import the function from main3.py, main2.py, main1.py
from main3 import text_to_speech
from main2 import text_to_text
from main1 import voice_to_text

#Initialise the Flask application
app = flask.Flask(__name__)

#Set the configuration for the uploads folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = 'uploads' 
#This might be used to store processed output files that can be served statically.
app.config['OUTPUT_FOLDER'] = 'static'

#Ensure the upload folder exists
if not os.path.exists('uploads'):
    os.mkdir('uploads')
if not os.path.exists('static'):
    os.mkdir('static')    

#Define the route for the homepage of the Flask app
@app.route('/')
def index(): #This function executed when the homepage is accessed.
    #The 'render_template' function is used to generate HTML response for the browser
    return flask.render_template('index.html')


#Function: 'process()' function handles the file upload
#Defines route for processing audio files, only allowing POST requests.
@app.route('/process', methods=['POST'])
def process():
    #Check if the 'audio' file is present in the request
    if 'audio' not in flask.request.files:
        return 'No audio file part', 400
    
    file = flask.request.files['audio']

    if file.filename == '':
        return "No selected file", 400
    

    #If file is present, following block will be executed
    if file:
        #Construct the file path for saving the uploaded file to 'UPLOAD_FOLDER'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        #Save the uploaded file to specificed path
        file.save(file_path)
        #Redirecs to the get_response route, passing the filename as a parameter
        return flask.redirect(flask.url_for('get_response', filename=file.filename))
    

#Function: 'get_response()' function processes the uploaded file:    
#Defines the route for processing a specific audio file, identified by its filename
@app.route('/process/<filename>')
def get_response(filename):    #This function is executed when the /process/<filename> route is accessed.
    input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #Construct the output path for the processed audio file.
    output_audio_path = os.path.join(app.config['OUTPUT_FOLDER'], 'response.wav')

    print(input_file_path)
    print(output_audio_path)
    
    #First call function to transfer voice to trancsript
    transcript_text = voice_to_text(input_file_path)

    #Then, with the output of the previous step, generate text
    generated_text = text_to_text(transcript_text)
    print(generated_text)
    # Process the audio file using your existing code in main3.py
    output_text = text_to_speech(generated_text, output_audio_path)

    return flask.render_template('index.html', text=output_text, audio_url=flask.url_for('static', filename='response.wav')) 


#Flask application runs only if the script is executed directly (not imported as a module).
if __name__ == '__main__':
    #Runs the Flask application in debug mode, which provides helpful error messages and automatic reloading.
    app.run(debug=True)