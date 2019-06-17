from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def detail(request, question_id):
    return HttpResponse("you are looking at the question %s" % question_id )

def results(request, question_id):
    return HttpResponse("you are looking at the result of question %s" % questiom_id)

def vote(request, question_id):
    return HttpResponse("you are votig on question %s" % question_id) 
