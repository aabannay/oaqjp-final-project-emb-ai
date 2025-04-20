"""Module providing a function to detect emotions in text."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion scores and the
        dominant emotion by name.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!!'
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {anger_score}," \
    f" 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and " \
    f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    #serving the app at port 5000!
    app.run(host="0.0.0.0", port=5000)
    