# -- coding: utf-8 --

from flask import Flask, render_template, request, Response
import requests
import string

app = Flask(__name__)

client_id = "as77sn9asj"
client_secret = "W9Jo2sJK7x4br8MnkHxl1NrW7fV7OU88XgNCbxKT"

def stt(data):
    resp_text = ""
    lang = "Kor"
    stt_url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,

        "Content-Type": "application/octet-stream"
    }


    response = requests.post(stt_url,  data=data, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        resp_text = response.text.split(":")[1].split("}")[0].strip(string.punctuation)
        print (response.text)
        
    else:
        resp_text = response.text
        print("Error : " + response.text)
    
    return resp_text

def papago(text):
    resp_text = ""
    papago_url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"    

    val = {
        "source": 'ko',
        "target": 'en',
        "text": text
    }

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }

    response = requests.post(papago_url,  data=val, headers=headers)
    rescode = response.status_code

    if(rescode == 200):
        resp_text = response.json()['message']['result']['translatedText']
        print(resp_text)
        
    else:
        print("Error : " + response.text)


    return resp_text

def tts(text):
    speaker = "clara"
    speed = "0"
    pitch = "0"
    emotion = "0"
    format = "wav"

    val = {
        "speaker": speaker,
        "speed": speed,
        "text": text,
        "format": format
    }

    tts_url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(tts_url,  data=val, headers=headers)
    rescode = response.status_code
    
    if(rescode != 200):
        return {"result_code":rescode}

    return response.content


@app.route("/")
def render_vt_page():
    return render_template('voice_translation.html')

@app.route('/trans', methods=['POST'])
def translate():
    file = request.files['file']
    data = file.read()
    
    stt_text = stt(data)
    papago_text = papago(stt_text)
    audio_data = tts(papago_text)
    
    return Response(audio_data, mimetype="audio/wav")
    
  

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080, ssl_context='adhoc')
