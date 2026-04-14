import requests
import json

def emotion_detector(text_to_analyse):
    '''This function passes text_to_analyze to Watson AI 
       and instructs it to use its Emotion Predict function.
    '''
    
    #Define the URL, headers, and dictionary needed to query Watson's Emotion Predict to analyze the text_to_analyze
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    #Pass the request to Watson and collect the response
    response = requests.post(url, json = myobj, headers=header)
    
    #Setting to manually test error handling.
    test_mode = True

    #If statement to assess whether to return the error response or proceed with formatting.
    if response.status_code == 400 or test_mode == True:
        emotion_scores = {'anger' : 'None', 'disgust' : 'None', 'fear' : 'None',
        'joy' : 'None', 'sadness' : 'None', 'dominant_emotion' : 'None'}
    else:
        #Format the response
        formatted_response = json.loads(response.text)

        #Filter through the response to the isolate the emotion scores.
        emotion_scores = formatted_response['emotionPredictions'][0]["emotion"]
    
        #Initialize placeholders for the top score
        top_score = 0
        dominant_emotion = 'None'
        #Loop through the raw scores to find the dominant emotion
        for emotion, score in emotion_scores.items():
            if score > top_score:
                top_score = score
                dominant_emotion = emotion
    

        #Append the dominant emotion to the scores dictionary and return it as an output.
        emotion_scores['dominant_emotion'] = dominant_emotion


        return emotion_scores