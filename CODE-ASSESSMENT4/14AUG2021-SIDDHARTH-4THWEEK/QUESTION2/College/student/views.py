from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def addStudent(request):
    if(request.method=="POST"):
        getname=request.POST.get("name")
        getadmin=request.POST.get("admin")
        getroll=request.POST.get("roll")
        getcollege=request.POST.get("college")
        getpame=request.POST.get("pname")
        mydict={"name":getname,"admin":getadmin,"roll":getroll,"college":getcollege,"pname":getpame}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("GET method got runned")

# Create your views here.
