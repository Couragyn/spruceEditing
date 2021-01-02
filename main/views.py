from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail


def send_contact(request):
	name = request.POST.get("nameInput")
	email = request.POST.get("emailInput")
	phone = request.POST.get("phoneInput")
	message = request.POST.get("messageInput")
 
	send_mail("New Contact Form Message", message, email, ["SpruceEditing@gmail.com"],
	html_message="<html>You received a new message from the contact form. </ br> Name:" + name + "Email Address:" + email + "Phone:" + phone + "&lt;br/&gt;Message:" + message + "</html>")
	request.session['sendmessage'] = "Message Has Been Sent"

	return HttpResponseRedirect('../contact/')

def contact_page(request):
	return render(request, "contact.html")