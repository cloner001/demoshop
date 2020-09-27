from django.shortcuts import render,HttpResponse
from .models import Product,Contact,Orders,updateOrder
from math import ceil
import json

def home(request):
    product = Product.objects.all()
    allProds = [ ]
    catprod = Product.objects.values('category','id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlide = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlide),nSlide])
    param = {'allProds' : allProds}
    return render(request,'shop/home.html',param)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def search(request):
    return render(request,'shop/search.html')

def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id = orderid,Email=email)
            if len(order)>0:
                update = updateOrder.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc , 'time': item.timestamp})
                    response = json.dumps([updates,order[0].Itemjson],default=str)
                return HttpResponse(response)
            else :
                return HttpResponse('Error')
        except Exception as e:
            return HttpResponse('Error')
    return render(request,'shop/tracker.html')

def productView(request,myid):
    product = Product.objects.filter( id = myid)

    return render(request,'shop/productView.html',{'product' : product[0] })

def checkout(request):
    if request.method == "POST":
        itemjson = request.POST.get('itemjson','')
        name= request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        zip_code=request.POST.get('zip_code','')
        state=request.POST.get('state','')
        order = Orders(Itemjson=itemjson,Name=name,Email=email,City=city,Phone=phone,Address=address,Zip_code=zip_code,State=state)
        order.save()
        update = updateOrder(order_id=order.order_id,update_desc="Order Has Been Placed")
        update.save()
        thanks = True
        id = order.order_id


        return render(request, 'shop/checkout.html',{'thanks':thanks , 'id' : id})
    return render(request,'shop/checkout.html')

def thank(request):
    if request.method == "POST":
        name= request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        desc =request.POST.get('desc','')

        contacts = Contact(name=name,email=email,description=desc,number=number)
        contacts.save()
    return render(request,'shop/thank.html')
