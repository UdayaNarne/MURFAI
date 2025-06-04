from flask import Flask, request, jsonify,send_file
from flask_cors import CORS

import os
import io
from dotenv import load_dotenv
from playsound import playsound
from transformers import pipeline
from langdetect import detect
from murf import Murf

load_dotenv()
API_KEY=os.getenv("API_KEY")
client=Murf(
    api_key=API_KEY,
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def get_overall_emotion(text):
    scores = classifier(text)[0]
    top_emotion = max(scores, key=lambda x: x['score'])
    return top_emotion['label'], top_emotion['score']

def match_tone_language(text):
    # Detect language
    language = detect(text)
    
    # Detect emotion
    emotion, confidence = get_overall_emotion(text)
    
    emotion_to_style = {
        'sad': 'Sad',
        'anger': 'Angry',
        'disgust': 'Sorrowful',
        'fear': 'Terrified',
        'joy': 'Meditative',
        'neutral': 'Calm'
    }
    style = emotion_to_style.get(emotion.lower(), "Conversational")

    language_to_voice = {
        'en': 'en-US-natalie',
        'hi': 'hi-IN-neerja',
        'es': 'es-ES-elvira',
        'fr': 'fr-FR-denise',
    }
    voice_id = language_to_voice.get(language, 'en-US-natalie')

    return voice_id, style, language, emotion

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Server is running"})

@app.route("/read-text", methods=["POST"])
def read_text():
    print("Received request to read text")
    data=request.get_json()
    text=data.get("text","")

    if not text.strip():
        return jsonify({"error":"No text selected"}),400
    
    voice_id, style, language, emotion = match_tone_language(text)
    print(f"Language: {language}, Emotion: {emotion}, Style: {style}, Voice: {voice_id}")

    audio_buffer = io.BytesIO()
    res = client.text_to_speech.stream(
        text=text,
        voice_id=voice_id,
        style=style
    )
    for chunk in res:
        audio_buffer.write(chunk)

    audio_buffer.seek(0)
    # output_file = "output.mp3"
    # with open(output_file, "wb") as f:
    #     f.write(audio_buffer.read())

    # print(f"Audio saved to {output_file}")
    # playsound(output_file)
    return send_file(audio_buffer,mimetype="audio/mpeg",download_name="result.mp3",as_attachment=False)
    # return jsonify({"message":"Audio generated and played successfully"}),200

if __name__ == "__main__":
    app.run(port=5000)