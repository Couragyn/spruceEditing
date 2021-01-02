from django import forms

quote_choices = [
    ('Academic Papers', 'Academic Papers'),
    ('Applications & Grants', 'Applications & Grants'),
    ('Cover letters & Resumes', 'Cover letters & Resumes'),
    ('Websites & Blogs', 'Websites & Blogs'),
    ('Newspaper & Magazine Articles', 'Newspaper & Magazine Articles'),
    ('Short- & Long-form Fiction', 'Short- & Long-form Fiction'),
    ('Short- & Long-form Creative Nonfiction', 'Short- & Long-form Creative Nonfiction'),

]

class ContactForm(forms.Form):
	name = forms.CharField(max_length=80)
	email = forms.EmailField()
	phone= forms.CharField(max_length=15, required=False)
	message = forms.CharField(widget=forms.Textarea)
	attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

class QuoteForm(forms.Form):
	name = forms.CharField(max_length=80)
	email = forms.EmailField()
	type_of_work = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=quote_choices,
    )
	details_for_quote = forms.CharField(widget=forms.Textarea)
	documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)