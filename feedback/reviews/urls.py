from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you/", views.ThankYouView.as_view(), name="thank_you"),
    path("review-list/", views.ReviewListView.as_view(), name="review_list"),
    path("single-review/<int:pk>/", views.SingleReviewView.as_view(), name="single_review"),
]
