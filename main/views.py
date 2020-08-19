
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList

# Create your views here.
@login_required(login_url='/login/')
def index(response,id):
    if id>len(ToDoList.objects.all()):
        return HttpResponse('list doesnot exists at all')
    ls=ToDoList.objects.get(id=id)

    if response.method== 'POST':
        print(response.POST)
        if response.POST.get('save'):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id))=='clicked':
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get('newItem'):
            txt=response.POST.get('new')
            #print(txt,ls,ls.item_set.all(),len(ls.item_set.get(text=txt)))
            if len(txt)>=2 and  len(ls.item_set.filter(text=txt))==0:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("Invalid")
    return render(response,'main/list.html',{'ls':ls})
#def v1(response):
#    return HttpResponse('view 1 !')quit
def home(response):
    return render(response,'main/home.html',{})
@login_required(login_url='/login/')
def create(response):
    if response.method=='POST':
        form=CreateNewList(response.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            t=ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect('/%i'%(t.id))
    else:
        form=CreateNewList()
    return render(response,'main/create.html',{'form':form})
@login_required(login_url='/login/')
def view(response):
    return render(response,'main/view.html',{})
