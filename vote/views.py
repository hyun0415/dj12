from django.shortcuts import render, redirect
from vote.models import Topic, Choice

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    t = Topic.objects.all()
    context = {
        "tset":t
    }
    return render(request, 'vote/index.html', context)

def detail(request, tpk):
    if request.user.is_anonymous:
        return redirect("acc:login")
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t": t,
        "cset": c,        
    }
    return render(request, 'vote/detail.html', context)

def vote(request, tpk):
    if request.user.is_anonymous:
        return redirect("acc:login")
    u = request.user
    t = Topic.objects.get(id=tpk)
    
    if not request.user in t.voter.all():
        t.voter.add(u)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.choicer.add(u)

    return redirect("vote:detail", tpk)

def create(request):
    if request.user.is_anonymous:
        return redirect("acc:login")
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        # print(s, c)
        t = Topic(subject=s, maker=request.user, content=c)
        t.save()
        cn = request.POST.getlist("cname")
        cc = request.POST.getlist("com")
        for name, comment in zip(cn, cc):
            Choice(top=t, name=name, comment=comment).save()
        return redirect("vote:index")
    return render(request, "vote/create.html")

def cancel(request, tpk):
    if request.user.is_anonymous:
        return redirect("acc:login")
    u = request.user
    t = Topic.objects.get(id=tpk)
    t.voter.remove(u)
    u.choice_set.get(top=t).choicer.remove(u) # 내가 선택한 초이스 레코드 중에서 제거
    return redirect("vote:detail", tpk)

def delete(request, tpk):
    if request.user.is_anonymous:
        return redirect("acc:login")
    t = Topic.objects.get(id=tpk)
    if t.maker == request.user:  
        t.delete()
    else:
        pass # 해킹!
    return redirect("vote:index")
