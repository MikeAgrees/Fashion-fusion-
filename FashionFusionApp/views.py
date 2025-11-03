from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *
from django.conf import settings
import os
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,"about.html") 

def shop_details(request):
    return render(request,"shop-details.html")

def blog_details(request):
    return render(request,"blog-details.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"blog-details.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        # Check if user with provided email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'User already exists; Please Consider To Login.'})

        # Create new user
        user = User(name=name, email=email, phone= phone_number ,password=password)
        user.save()
        return redirect('/login/?status=1')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()

        if user is not None:
            if user.password == password:
                request.session['id'] = user.id
                request.session['username'] = user.name
                request.session['email'] = user.email
                request.session['usercart']=[]
                request.session['cartcount']=0
                products = ProductStock.objects.all()
                return render(request,'index.html',{'products':products,'status':1})
            return render(request, 'login.html', {'password_error': True,'error':'Wrong Password!!!'})
            
        else:
            return render(request, 'login.html', {'email_error':True,'error': 'Invalid Email ID!!!'})

    return render(request, 'login.html')

from django.http import JsonResponse
import json
def addToCart(request):
    if request.method == 'POST':
        try:
            data =json.loads(request.body)  # If the data is sent as JSON
            # Add to user cart
            request.session['usercart'].append(data)
            request.session['cartcount']+=1
            print(request.session['usercart'])
            return JsonResponse({'message': 'Data received successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
import time     
def checkout(request):
    if request.method=='POST':
        # Introduce a 5-second delay
        time.sleep(5)
        return render(request,"successPage.html")
    return render(request,'checkout.html')

def shoppingCart(request):
    user_cart_products=request.session['usercart']
    user_cart_count=request.session['cartcount']
    print(user_cart_products)
    context={
        "user_cart_count":user_cart_count,
        "user_cart_products":user_cart_products
    }
    return render(request,'shopping-cart.html',context)

def updateCart(request):
    if request.method=='POST':
        data = json.loads(request.body)
        for product in request.session['usercart'] :
            if product['id'] == data.get("productId") :
                product['qty'] = data.get("newQuantity")
                product['total'] = float(data.get("newTotalPrice"))
                print(f"Updated : {request.session['usercart']}")
                request.session['usercart'].append(product)
                
                break
        print(f"Updated : {request.session['usercart']}")
        return JsonResponse({'msg': request.session['usercart']})
    return JsonResponse({"error": "Invalid Request!!!"})

def removeFromCart(request):
    if request.method=="POST":
        data =json.loads(request.body)
        products = request.session['usercart']
        products = [product for product in products if product['id'] not in list(data.get('productId'))]
        request.session['usercart'] = products
        return JsonResponse({'msg': request.session['usercart']})
    return JsonResponse({'msg':"failed"})

def logout(request):
    del request.session['id']
    del request.session['email']
    del request.session['username']
    del request.session['usercart']
    del request.session['cartcount']
    return redirect('/')

def crud_view(request):
    stocks = ProductStock.objects.all()
    return render(request,'crud_view.html',{'stocks':stocks})

def add(request):
    if request.method == "POST":
        name = request.POST.get('p_name')
        price = request.POST.get('p_price')
        # Access the uploaded file
        uploaded_file = request.FILES.get('p_image')
        if uploaded_file:
            # Save the uploaded file to the specified location
            file_storage = FileSystemStorage(location=settings.MEDIA_ROOT + '/static/img/products/')
            file_path = 'static/img/products/' + uploaded_file.name
            file_storage.save(uploaded_file.name, uploaded_file)
            # Store the file path in the database
            product = ProductStock.objects.create(name=name, price=price, image=file_path)
            if product:
                return HttpResponseRedirect('/add/?success=True')
            else:
                return HttpResponseRedirect('/add/?error=True')
    return render(request, 'add.html')

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')

def edit(request):
    return render(request,'edit.html')

def delete_inline(request):
    return render(request,'delete.html')