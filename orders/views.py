from django.shortcuts import render, redirect
from .models import Order
from django.db.models import Sum


# Home Page
def index(request):
    return render(request, "index.html")


# Order Page
def order(request):
    return render(request, "order.html")


# Payment Page
def payment(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        product = request.POST.get("product")
        quantity = request.POST.get("quantity")
        total = request.POST.get("total")

        request.session['name'] = name
        request.session['phone'] = phone
        request.session['address'] = address
        request.session['product'] = product
        request.session['quantity'] = quantity
        request.session['total'] = total

    return render(request, "payment.html")


# Scanner Page
def scanner(request):

    data = {
        "name": request.session.get("name"),
        "phone": request.session.get("phone"),
        "address": request.session.get("address"),
        "product": request.session.get("product"),
        "quantity": request.session.get("quantity"),
        "total": request.session.get("total")
    }

    return render(request, "scanner.html", data)


# Success Page
def success(request):

    name = request.session.get("name")
    phone = request.session.get("phone")
    address = request.session.get("address")
    product = request.session.get("product")
    quantity = request.session.get("quantity")
    total = request.session.get("total")
    payment = request.GET.get("payment")

    Order.objects.create(
        name=name,
        phone=phone,
        address=address,
        product=product,
        quantity=quantity,
        total=total,
        payment=payment
    )

    return render(request,"success.html",{
        "name":name,
        "phone":phone,
        "address":address,
        "product":product,
        "quantity":quantity,
        "total":total,
        "payment":payment
    })


# Contact Page
def details(request):
    return render(request, "details.html")


# Admin Login
def admin_login(request):

    error = ""

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        if username == "admin" and password == "admin@12345":

            request.session["admin"] = "admin"

            return redirect("/dashboard")

        else:

            error = "Invalid ID or Password"

    return render(request, "admin_login.html", {"error": error})


# Admin Dashboard
def dashboard(request):

    if not request.session.get("admin"):
        return redirect("/admin-login")

    orders = Order.objects.all().order_by('-date')

    online_total = Order.objects.filter(payment="Online").aggregate(Sum('total'))

    cod_total = Order.objects.filter(payment="Cash").aggregate(Sum('total'))

    grand_total = Order.objects.aggregate(Sum('total'))

    return render(request, "dashboard.html", {
        "orders": orders,
        "online_total": online_total,
        "cod_total": cod_total,
        "grand_total": grand_total
    })


# Delete Order
def delete_order(request, id):

    Order.objects.get(id=id).delete()

    return redirect("/dashboard")
def online(request):

    return render(request,"online.html",{

        "name":request.session.get("name"),
        "phone":request.session.get("phone"),
        "address":request.session.get("address"),
        "product":request.session.get("product"),
        "quantity":request.session.get("quantity"),
        "total":request.session.get("total")

    })
