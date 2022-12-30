from django.shortcuts import render
from googletrans import LANGUAGES
from gtts import gTTS
from random import sample

# Create your views here.

def make():
    l = "0123456789qwertyuiopasdfghjklzxcvbnm"
    st = ""
    for i in range(10):
        st += sample(l, 1)[0]
    return st



def index(request):
    context= {
    'ndict' : LANGUAGES
    }
    if request.method == "POST":
        c = request.POST.get("con")
        n = request.POST.get("ncode")
        tts = gTTS(c, lang=n)
        filename = make()
        tts.save('media/tts/hello.mp3')
        context.update({
            "bf":c,
            "to":n,
            "fn":filename
        })
    return render(request, "tts/index.html", context)