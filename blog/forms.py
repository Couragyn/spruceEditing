from .models import Comment
from django import forms
from captcha.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {
	        "body": "Comment"
	    }
    captcha = ReCaptchaField()

