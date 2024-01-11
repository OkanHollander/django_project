from django.shortcuts import render

# Create your views here.
def reviewer(request):
    return render(request, "reviews/review.html")
