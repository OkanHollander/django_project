from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This is the month January",
    "February": "This is the month February",
    "march": "This is the month March",
    "april": "This is the month April",
    "may": "This is the month May",
    "june": "This is the month June",
    "july": "This is the month July",
    "august": "This is the month August",
    "september": "This is the month September",
    "october": "This is the month October",
    "november": "This is the month November",
    "december": "This is the month December",
}


# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month does not exist.</h1>")
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
