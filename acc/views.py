from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User
import googletrans
from googletrans import Translator

# Create your views here.
def index(request):
    return render(request, 'acc/index.html')

def ulogin(request): # 함수명에 login 사용하면 안됨
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        # print (un, up)
        # print( authenticate(username=un, password=up) )
        u = authenticate(username=un, password=up) # 인증정보 유무를 확인하고 제대로 로그인 되면 레코드를 반환, 실패하면 None
        if u: # 인증에 성공했다면!
            login(request, u) # request user에(계정정보 포함) u레코드를 끼워준다
            #print(request.user)
            messages.success(request, f"{un}님 환영합니다!!")
            return redirect("acc:index")
        else:
            messages.error(request, "계정정보가 일치하지 않습니다")
            pass # 마지막날

    return render(request, "acc/login.html")

def ulogout(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    logout(request) # request.user 에서 user 레코드를 빼냄
    return redirect("acc:index")

def profile(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    return render(request, "acc/profile.html")

def delete(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    u = request.user
    ck = request.POST.get("ckpass")
    # print(ck)
    # print(check_password(ck, u.password))
    if check_password(ck, u.password)==True:
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    return redirect("acc:profile")

def signup(request): #create
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucom")
        pi = request.FILES.get("upic")
        # print (un, up)
        try: #시도하다가 에러가 나면 except로 빠짐, 유니크 필드가 중복되는 걸 방지
            User.objects.create_user(username=un, password=up, comment=uc, pic=pi) #테이블 조회하듯이 만들면 안됨
            return redirect("acc:login")
        except:
            pass # 나중에 사용자들에게 안내 
    return render(request, "acc/signup.html")

def chpass(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    if request.method == "POST":
        u = request.user
        cp = request.POST.get("cpass")
        if check_password(cp, u.password):
            np = request.POST.get("npass")
            u.set_password(np)
            u.save()
            return redirect("acc:login")
    return redirect("acc:update")


def update(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    if request.method == "POST":
        u = request.user
        ue = request.POST.get("umail")
        uc = request.POST.get("ucom")
        up = request.FILES.get("upic")
        # print(ue, uf, ul)
        u.email, u.first_name = ue, uc # request.user에서 끌어올 수 있음
        if up: # u.pic의 경우 초기값이 없음. 새로운 사진이 있을 경우에만 갱신
            u.pic.delete()
            u.pic = up
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")


