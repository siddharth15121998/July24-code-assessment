from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from books.models import Book
from books.serializers import BookSerializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_api(request):
    if(request.method=='POST'):
        mydata=JSONParser().parse(request)
        book_serialize=BookSerializers(data=mydata)
        if(book_serialize.is_valid()):
            book_serialize.save()
            return JsonResponse(book_serialize.data)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("no GET method is allowed")

@csrf_exempt
def viewall_api(request):
    if(request.method=='GET'):
        b1=Book.objects.all()
        book_serialize=BookSerializers(b1,many=True)
        return JsonResponse(book_serialize.data,safe=False)

@csrf_exempt
def view_api(request,name):
    try:
        b1=Book.objects.get(name=name)
    except Book.DoesNotExist:
        return HttpResponse("Invalid book name")

    if(request.method=='GET'):
        book_serialize=BookSerializers(b1)
        return JsonResponse(book_serialize.data,safe=False)

    if(request.method=='PUT'):
        
        mydata=JSONParser().parse(request)
        book_serialize=BookSerializers(b1,data=mydata)
        if(book_serialize.is_valid()):
            book_serialize.save()
            return JsonResponse(book_serialize.data)
        
        else:
            return HttpResponse("something went wrong ")

    if(request.method=='DELETE'):
        b1.delete()
        return HttpResponse("Donor deleted")


def registerbooks(request):
    return render(request,'addbook.html')



