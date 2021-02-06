from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Pay
from django.views import generic
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

def process_payment(request, id):
    order = get_object_or_404(Pay, id=id)

    if order.paid == True:
    	request.invoice = order.id
    	return render(request, 'payment_done.html')

    else:
	    host = request.get_host()
	    order.currency_type = order.get_currency_display()

	    paypal_dict = {
	        'business': settings.PAYPAL_RECEIVER_EMAIL,
	        'amount': str(order.amount),
	        'item_name': order.description,
	        'invoice': str(id),
	        'currency_code': order.currency_type,
	        'notify_url': 'http://{}{}'.format(host,
	                                           reverse('paypal-ipn')),
	        'return_url': 'http://{}{}'.format(host,
	                                           reverse('payment_done')),
	        'cancel_return': 'http://{}{}'.format(host,
	                                              reverse('payment_cancelled')),
	    }

	    form = PayPalPaymentsForm(initial=paypal_dict)
	    return render(request, 'process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
        #...
        #...

            return redirect('process_payment')


    else:
        form = CheckoutForm()
        return render(request, 'checkout.html', locals())
