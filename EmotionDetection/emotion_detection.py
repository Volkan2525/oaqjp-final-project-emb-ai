import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)

    jrespone = json.loads(response.text)
    anger = jrespone['emotionPredictions'][0]['emotion']['anger']
    disgust = jrespone['emotionPredictions'][0]['emotion']['disgust']
    fear = jrespone['emotionPredictions'][0]['emotion']['fear']
    joy = jrespone['emotionPredictions'][0]['emotion']['joy']
    sadness = jrespone['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(anger,disgust,fear,joy,sadness)

    if dominant_emotion == anger:
        d_emotion = "anger"
    elif dominant_emotion == disgust:
        d_emotion = "disgust"
    elif dominant_emotion == fear:
        d_emotion = "fear"
    elif dominant_emotion == joy:
        d_emotion = "joy"
    elif dominant_emotion == sadness:
        d_emotion = "sadness"
    return {"anger":anger, "disgust":disgust, "fear":fear, "joy":joy, "sadness":sadness,"The dominant emotion is":d_emotion}