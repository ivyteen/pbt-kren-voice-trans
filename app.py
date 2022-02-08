# -- coding: utf-8 --

from flask import Flask, render_template, request, Response
import requests
import string

app = Flask(__name__)

client_id = ""
client_secret = ""


@app.route("/")
def render_vt_page():
    return render_template('voice_translation.html')

@app.route('/trans', methods=['POST'])
def translate():
    
    #미션 : 아래 힌트와 API 예제 코드를 활용하여 한영 동시 통역기를 구현하고, 
    # 구현내용을 정리하여 발표하세요
    
    #힌트 1 (STT 오디오 입력)
    #file = request.files['file']
    #data = file.read()

    #힌트 2 (STT 응답에서 추출)
    #resp_text = response.text.split(":")[1].split("}")[0].strip(string.punctuation)

    #힌트 3 (번역 API 요청 파라미터)
    #https://api.ncloud-docs.com/docs/ai-naver-papagonmt-translation 참고
    
    #힌트 4 (TTS 요청 파라미터)
    #https://api.ncloud-docs.com/docs/ai-naver-clovavoice-ttspremium 참고
    #음성 포맷(format)은 wav를 사용하세요
    
    #힌트 5 (TTS 응답 리턴)
    #return Response(response.content, mimetype="audio/wav")
    
    return


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080, ssl_context='adhoc')
