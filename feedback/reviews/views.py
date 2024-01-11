from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request,):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form})
    
    def post(self, request,):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
        "form": form})

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Thank you for your review!"
        return context
    

# def reviewer(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data["user_name"],
#             #                 review_text=form.cleaned_data["review_text"],
#             #                 rating=form.cleaned_data["rating"])
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {
#         "form": form})

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
