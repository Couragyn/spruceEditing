from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail


def send_contact(request):
	name = request.POST.get("name")
	email = request.POST.get("email")
	subject = request.POST.get("subject")
	message = request.POST.get("message")
 
	send_mail("New Contact Form Message", message, email, ["SpruceEditing@gmail.com"],
	html_message="<html>You received a new message from the contact form. </ br> Name:" + name + "Email Address:" + email + "Subject:" + subject + "&lt;br/&gt;Message:" + message + "</html>")
	request.session['sendmessage'] = "Message Has Been Sent"

	return HttpResponseRedirect('../contact/')

def contact_page(request):
	return render(request, "contact.html")