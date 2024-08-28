from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/")
def render_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    txt = request.args.get('textToAnalyze')
    return emotion_detector(txt)

app.run(host="0.0.0.0",port=5000)