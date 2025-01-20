"""
This module uses emotion detection API. It creates a Flask application that
processes user text and returns values of detected emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app=Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    """
    Retrieves text after a request, passes text to emotion detector, and
    returns a formatted response of the emotion values and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    joy = response['joy']
    anger = response['anger']
    fear=response['fear']
    disgust=response['disgust']
    sadness=response['sadness']
    dominant=response['dominant_emotion']
    if dominant is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
@app.route("/")
def render_index_page():
    """Renders index HTML page of emotion detector website."""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
