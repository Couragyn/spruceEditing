from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from .forms import UploadForm
from django.views import View


# def send_contact(request):
# 	name = request.POST.get("nameInput")
# 	email = request.POST.get("emailInput")
# 	phone = request.POST.get("phoneInput")
# 	message = request.POST.get("messageInput")

# 	email_body = "<html>You received a new message from the contact form. </ br> Name:" + name + "Email Address:" + email + "Phone:" + phone + "&lt;br/&gt;Message:" + message + "</html>"

# 	full_email = EmailMessage("New Contact Form Message", email_body, email, ["SpruceEditing@gmail.com"])

# 	form = UploadForm(request.POST, request.FILES)
# 	files = request.FILES.getlist('attached[]')
# 	for f in files:
# 		full_email.attach(f.name, f.read(), f.content_type)

# 	full_email.send()
# 	request.session['sendmessage'] = "Message Has Been Sent"

# 	return HttpResponseRedirect('../contact/')


class contact_page_view(View):
	form_class = UploadForm
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
			attached = request.FILES.getlist('file_field')

			try:
				email_body = "<html>You received a new message from the contact form. </ br></ br> Name:" + name + "Email Address:" + email + "Phone:" + phone + "&lt;br/&gt;Message:" + message + "</html>"
				mail = EmailMessage("New Contact Form Message", email_body, email, ["SpruceEditing@gmail.com"])
				for f in attached:
					mail.attach(f.name, f.read(), f.content_type)
				mail.send()
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Email successfully sent to SpruceEditing@gmail.com'})
			except:
				return render(request, self.template_name, {'email_form': form, 'error_message': 'Error sending email. Please try again later. Please make sure attachements are under 10mb'})

		return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

    # Single File Attachment
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)

    #     if form.is_valid():
            
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         attach = request.FILES['attach']

    #         try:
    #             mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    #             mail.attach(attach.name, attach.read(), attach.content_type)
    #             mail.send()
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
    #         except:
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

    #     return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})








# def contact_page(request):
# 	return render(request, "contact.html")