from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "February": "Walk for at least 20 minutes a day",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes a day",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes a day",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes a day",
    "december": None,
}


def month_keys():
    months = list(monthly_challenges.keys())
    return months


def reverse_month_path(redirect_month):
    return reverse("monthly_challenge", args=[redirect_month])


# Create your views here.
def index(request):
    months = month_keys()

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        return render(
            request,
            "challenges/challenge.html",
            {
                "challenge_text": challenge_text,
                "month_text": month,
            },
        )
    except Exception as exc:
        raise Http404() from exc


def monthly_challenge_by_number(request, month):
    months = month_keys()
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse_month_path(redirect_month)

    return HttpResponseRedirect(redirect_path)
