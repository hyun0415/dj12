'''
import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)

translator = Translator()
text1 = "Hello welcome to my website!"
trans1 = translator.translate(text1, src='en', dest='ko')

print("English to Korean:", trans1.text)
'''

from gtts import gTTS
from googletrans import Translator as tr

st = """26일 국토교통위원회 소속 박상혁 더불어민주당 의원이 HUG로부터 받은 자료에 따르면 ‘빌라왕’ 김씨와 관련한 전세보증금반환 보증보험 사고 건수는 지난달 말 기준으로 171건으로 집계됐다. 전세기간이 만료됐지만 세입자에게 보증금을 돌려주지 못한 건수가 171건이라는 얘기다. 이 중 91건은 김씨가 세운 법인 보유 주택에서 발생했으며, 나머지 80건은 김씨 명의 주택에서 보증사고가 났다."""""

a = tr.translate(st, src="en", dest="zh-cn")
tts = gTTS(st, lang="ko")
tts.save('hello.mp3')

dir(gTTS)
