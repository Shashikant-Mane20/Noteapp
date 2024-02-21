from django.shortcuts import render,HttpResponse,redirect
from noteapp.models import NoteList
from django.db.models import Q

# Create your views here.
def dashboard_page(request):
    return HttpResponse("Hello From Dashboard Page")


def home_page(request):
    n=NoteList.objects.filter(is_active=1)
    print(n)
    print(request.user) #entire object we can accessed from session
    print(request.user.id)
    print(request.user.username)
    print(request.user.is_superuser)
    print('Value:',request.user.is_authenticated)
    if request.user.is_authenticated:
        q1=Q(is_active=1)
        q2=Q(user_id=request.user.id)
        n=NoteList.objects.filter(q1 & q2)
        
        
        for x in n:
            print(x.id)
            print(x.title)
            print(x.date)
            print(x.desc)
        
        context={}
        context['data']=n
        return render(request,'noteapp/dashboard.html',context)
    else:
        return redirect('/authapp/login')


def add_notes(request):
    if request.method== "POST":
        t=request.POST['title']
        d=request.POST['dt']
        dt=request.POST['desc']
        print(t)
        print(d)
        print(dt)
        n=NoteList.objects.create(title=t,date=d,desc=dt,user_id=request.user)
        n.save()
        return redirect('/home')
        
    else:
        return render(request,'noteapp/add_notes.html')
    
def delete_notes(request,rid):
    # print(rid)
    # return HttpResponse("ID to be deleted:"+rid)
    # n=NoteList.objects.get(id=rid)
    # n.delete()
    # print(n)
    n=NoteList.objects.filter(id=rid)
    n.update(is_active=0)
    return redirect('/home')
    
        

def edit_notes(request,rid):

    if request.method == "POST":
        nt=request.POST['title']
        nd=request.POST['dt']
        ndt=request.POST['des']
        print("Updated Titles:",nt)
        print("Updated Date:",ndt)
        print("Updated Description:",ndt)
        n=NoteList.objects.filter(id=rid)
        n.update(title=nt,date=nd,desc=ndt)
        return redirect("/home")
    else:

        n=NoteList.objects.get(id=rid)
        context={}
        context['data']=n
        print(n)
        return render(request,'noteapp/edit_notes.html',context)
    
    return HttpResponse("Hello From edit Page")