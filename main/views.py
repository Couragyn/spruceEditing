from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from .forms import UploadForm
from .models import Document


def send_contact(request):
	request = request
	files = request.FILES
	post = request.POST
	name = request.POST.get("nameInput")
	email = request.POST.get("emailInput")
	phone = request.POST.get("phoneInput")
	message = request.POST.get("messageInput")
	attachments = request.POST.get("attached[]")

	# form = UploadFileForm(request.POST, request.FILES)
	# if form.is_valid():
	# 	form.save()

	# form = UploadForm(request.POST, request.FILES)
 #    files = request.FILES.getlist('attached[]')
	# if form.is_valid():
	# 	for f in files:
	# 		full_email.attach_file(f)
	# else:
	# 	form = UploadForm()



	email_body = "<html>You received a new message from the contact form. </ br> Name:" + name + "Email Address:" + email + "Phone:" + phone + "&lt;br/&gt;Message:" + message + "</html>"
 

	full_email = EmailMessage("New Contact Form Message", email_body, email, ["SpruceEditing@gmail.com"])

	form = UploadForm(request.POST, request.FILES)
	files = request.FILES.getlist('attached[]')
	# files1 = request.FILES.getlist()
	files21 = request.FILES
	if form.is_valid():
		for f in files:
			full_email.attach(f.name, f.read(), f.content_type)
	else:
		form = UploadForm()


	full_email.send()
	request.session['sendmessage'] = "Message Has Been Sent"

	return HttpResponseRedirect('../contact/')

def contact_page(request):
	return render(request, "contact.html")


# class contact_page(FormView):
# 	# return render(request, "contact.html")


# 	form_class = ContactForm
# 	template_name = 'contact.html'  
# 	success_url = '../contact/'

# 	def post(self, request, *args, **kwargs):
# 		form_class = self.get_form_class()
# 		form = self.get_form(form_class)
# 		files = request.FILES.getlist('file_field')
# 		if form.is_valid():
# 			for f in files:
# 				print(yo)
# 			return self.form_valid(form)
# 		else:
			# return self.form_invalid(form)