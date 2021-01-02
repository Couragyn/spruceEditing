from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from .forms import ContactForm, QuoteForm
from django.views import View


class contact_view(View):
	form_class = ContactForm
	template_name = 'contact.html'


	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'email_form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)

		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']
			attached = request.FILES.getlist('attachments')

			try:
				email_body = "<html>You received a new message from the contact form. </ br></ br> Name:" + name + "Email Address:" + email + "Phone:" + phone + "&lt;br/&gt;Message:" + message + "</html>"
				mail = EmailMessage("New Contact Form Message", email_body, email, ["SpruceEditing@gmail.com"])
				for f in attached:
					mail.attach(f.name, f.read(), f.content_type)
				mail.send()
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Email successfully sent to SpruceEditing@gmail.com'})
			except:
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Error sending email. Please make sure attachements are under 10mb and try again later. '})

		return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})


class quote_view(View):
	form_class = QuoteForm
	template_name = 'quote.html'


	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'email_form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)

		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			details_for_quote = form.cleaned_data['message']
			type_of_work = form.cleaned_data['type_of_work']
			documents = request.FILES.getlist('file_field')

			try:
				email_body = "<html>You received a new message from the contact form. </ br></ br> Name:" + name + "Email Address:" + email + "Details:" + details_for_quote + "&lt;br/&gt;Type of Work:" + type_of_work + "</html>"
				mail = EmailMessage("New Contact Form Message", email_body, email, ["SpruceEditing@gmail.com"])
				for f in attached:
					mail.attach(f.name, f.read(), f.content_type)
				mail.send()
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Email successfully sent to SpruceEditing@gmail.com'})
			except:
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Error sending email. Please make sure attachements are under 10mb and try again later. '})

		return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})