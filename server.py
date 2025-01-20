from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app=Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    joy = response['joy']
    anger = response['anger']
    fear=response['fear']
    disgust=response['disgust']
    sadness=response['sadness']
    dominant=response['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!"
    else:
        return "For the given statement, the system reponse is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}. The dominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant)
@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
