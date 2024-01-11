from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100,
#                                 label="Your Name",
#                                 error_messages={"required": "Please enter your name.",
#                                                 "max_length": "Your name must be 100 characters or less."})
#     review_text = forms.CharField(label="Your Feedback",
#                                   widget=forms.Textarea(),
#                                   max_length=250,)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["user_name", "review_text", "rating"]
        
