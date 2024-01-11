from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def reviewer(request):
    if request.method == "POST":
        entered_username = request.POST.get("username")
        if entered_username == "":
            return render(request, "reviews/review.html", context={"error": True})
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    return render(request, "reviews/review.html", context={"error": False})

def thank_you(request):
    return render(request, "reviews/thank_you.html")
