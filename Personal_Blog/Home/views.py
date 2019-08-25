from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
        Index in my Web Page
    """
    return HttpResponse("Hello! This is the Eder's Personal Blog")
