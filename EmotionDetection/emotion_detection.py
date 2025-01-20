import requests, json
def emotion_detector(text_to_analyze):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={"raw_document": { "text": text_to_analyze }}
    response=requests.post(url, json=myobj, headers=header)
    if response.status_code==400:
        formatted_emotions={
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        formatted_response=json.loads(response.text)
        emotions=formatted_response['emotionPredictions'][0]['emotion']
        anger_score=emotions['anger']
        disgust_score=emotions['disgust']
        fear_score=emotions['fear']
        joy_score=emotions['joy']
        sadness_score=emotions['sadness']
        max_score=max(emotions,key=emotions.get)
        formatted_emotions['dominant dictionary']=max_score
    return formatted_emotions