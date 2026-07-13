from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emo_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response
    if dominant_emotion == None:
        return 'Invalid text! Please try again!.'
    return (f"For the given statement, the system response is {response}")

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)