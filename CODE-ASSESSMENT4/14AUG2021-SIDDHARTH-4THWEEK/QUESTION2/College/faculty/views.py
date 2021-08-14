from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def addFaculty(request):
    if(request.method=="POST"):
        getnamee=request.POST.get("namee")
        getadd=request.POST.get("address")
        getdept=request.POST.get("dept")
        getcollegee=request.POST.get("collegee")
        mydict1={"namee":getnamee,"address":getadd,"dept":getdept,"collegee":getcollegee}
        result1=json.dumps(mydict1)
        return HttpResponse(result1)
    else:
        return HttpResponse("GET method got runned")


# Create your views here.
