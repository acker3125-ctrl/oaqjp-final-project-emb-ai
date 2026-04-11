from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def input_analyzer():
    #Retrieve text to analyze from the request
    text_to_analyze = request.args.get('textToAnalyze')
    
    #Pass the text to analyze to the emotion detector
    results = emotion_detector(text_to_analyze)
    

    
    #Format the output
    output = f"""For the given statement, the system response is 'anger': {results['anger']}, 
    'disgust': {results['disgust']}, 'disgust': {results['disgust']}, 'fear': {results['fear']}, 'joy': {results['joy']}, 
    'sadness': {results['sadness']}. The dominant emotion is {results['dominant_emotion']}."""
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)