from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is the month January"
    elif month == "february":
        challenge_text = "This is the month February"
    elif month == "march":
        challenge_text = "This is the month March"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)
