from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import razorpay
#from .models import TodoItem

first_time = True

# Create your views here.
def Home(request):
  return render(request, "index.html")

def Payment(request):
  client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

  data = { 
    "amount": 50000, 
    "currency": "INR", 
    "receipt": "order_rcptid_11" ,
    "payment_capture":"1"
    }
  payment = client.order.create(data=data)
  
  #order_id = payment['id']

  context = {
     'api_key':settings.RAZOR_KEY_ID, #'order_id':order_id
  }

  return render(request, "pay.html")
