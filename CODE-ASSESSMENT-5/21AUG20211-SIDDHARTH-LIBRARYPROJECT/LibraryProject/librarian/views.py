from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from librarian.models import Library
from librarian.serializers import LibrarySerializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_apii(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        lib_serialize=LibrarySerializers(data=mydata)
        if(lib_serialize.is_valid()):
            lib_serialize.save()
            return JsonResponse(lib_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("no GET method is allowed")

@csrf_exempt
def viewall_apii(request):
    if(request.method=='GET'):
        l1=Library.objects.all()
        lib_serialize=LibrarySerializers(l1,many=True)
        return JsonResponse(lib_serialize.data,safe=False)

@csrf_exempt
def view_apii(request,ecode):
    try:
        l1=Library.objects.get(ecode=ecode)
    except Library.DoesNotExist:
        return HttpResponse("Invalid ecode")

    if(request.method=='GET'):
        lib_serialize=LibrarySerializers(l1)
        return JsonResponse(lib_serialize.data,safe=False)

    if(request.method=='PUT'):
        
        mydata=JSONParser().parse(request)
        lib_serialize=LibrarySerializers(l1,data=mydata)
        if(lib_serialize.is_valid()):
            lib_serialize.save()
            return JsonResponse(lib_serialize.data)
        
        else:
            return HttpResponse("something went wrong ")

    if(request.method=='DELETE'):
        l1.delete()
        return HttpResponse("librarian deleted")


def registerlibrarian(request):
    return render(request,'registerlibrarian.html')

def loginlibrarian(request):
    return render(request,'loginlibrarian.html')




