from django import forms

class UploadForm(forms.Form):
	name = forms.CharField(max_length=80)
	email = forms.EmailField()
	phone= forms.CharField(max_length=15, required=False)
	message = forms.CharField(widget=forms.Textarea)
	file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
