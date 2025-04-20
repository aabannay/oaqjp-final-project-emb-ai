import json
import numpy as np
import requests

def emotion_detector(text_to_analyze):
    """
        takes a text to perform emotion detection and returns text attribute of response
    """
    #define the request load
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {'raw_document': {'text': text_to_analyze}}
    
    #get response
    response = requests.post(url, json = myobj, headers = header)
    emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None 
        }
    
    if response.status_code == 500 or response.status_code == 400: 
        return emotions 
    #format response text to json
    formatted_response = json.loads(response.text)

    #get emotion scores from json
    try: 
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    except KeyError: 
        return emotions

    #create a dictionary with the scores
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score 
    }
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    if response.status_code == 200: 
        return emotions