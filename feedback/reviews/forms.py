from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100,
                                label="Your Name",
                                error_messages={"required": "Please enter your name.",
                                                "max_length": "Your name must be 100 characters or less."})
