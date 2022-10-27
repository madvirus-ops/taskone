from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

db = {
    "slackUsername":"madvirus",
    "age":20,
    "bio":"web developer",
    "backend":True
}


def home(request):
    return JsonResponse(db)