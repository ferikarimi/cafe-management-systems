from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import TablesForm,OrdersForm,OrderDetailsForm,ReceiptForm
from .models import Tables,Orders,OrdersDetails,Reciepts
# Create your views here.
def tables_list_view(request):
    tables = Tables.objects.all()
    context = {'tables':tables}
    return render(request,"dashboard/dashboard_tables.html",context)


def tables_create_view(request):
    if request.method == "POST":
        form = TablesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tables_list")
    else:
        form = TablesForm()
    return render(request,"dashboard/table_create.html",{"form":form})

def tables_update_view(request,table_id):
    context = {}
    table_obj = Tables.objects.get(id=table_id)
    form = TablesForm(instance=table_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/dashboard/tables/")
    context['form'] = form
    return render(request,"dashboard/table_update.html",context)

def table_delete_view(request,table_id):
    context = {}
    table_obj = get_object_or_404(Tables,id=table_id)
    if request.method == "POST":
        table_obj.delete()
        return HttpResponseRedirect("/dashboard/tables")
    return render(request,"dashboard/table_delete.html",context)

def show_order_list(request):
    orders_obj = Orders.objects.all()
    context = {"orders":orders_obj}
    return render(request,"/",context=context)

def show_order_indetail(request,order_id):
    orders_indetail_obj = Orders.objects.get(id=order_id)
    context = {"order_indetail":orders_indetail_obj}
    return render(request,"/",context=context)

def create_order_view(request):
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("")
        else:
            form = OrdersForm()

        return render(request,"/",{"form":form})

def order_update_view(request,order_id):
    context = {}
    order_obj = Orders.objects.get(id=order_id)
    form = OrdersForm(instance=order_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("")
    context['form'] = form
    return render(request,"/",context)   

def order_delete_view(request,order_id):
    context = {}
    order_obj = get_object_or_404(Orders,id=order_id)
    if request.method == "POST":
        order_obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"/",context=context)

def order_details_list(request):
    order_details_obj = OrdersDetails.objects.all()
    context = order_details_obj
    return render(request,"/",context=context)

def order_details_indetail(request,orderdetail_id):
    order_details_obj = OrdersDetails.objects.get(id=orderdetail_id)
    context = order_details_obj
    return render(request,"/",context=context)

def create_orderdetail(request):
    if request.method == "POST":
        form = OrderDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("/")
        else :
            form = OrderDetailsForm()  

        return render(request,"/",{"form":form})    

def edit_orderdetail(request,orderdetail_id):
    context = {}
    orderdetail_obj = OrdersDetails.objects.get(id=orderdetail_id)
    form = OrderDetailsForm(instance=orderdetail_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("")
    context['form'] = form
    return render(request,"/",context)    

def delete_orderdetail(request,orderdetail_id):
    context = {}
    orderdetail_obj = get_object_or_404(Orders,id=orderdetail_id)
    if request.method == "POST":
        orderdetail_obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"/",context=context)  

def receipt_show_list(request):
    receipts_obj = Reciepts.objects.all()
    context = receipts_obj
    return render(request,"/",context=context)

def receipt_show_indetail(request,receipt_id):
    receipt_obj = Reciepts.objects.get(id=receipt_id)
    context = receipt_obj
    return render(request,"",context=context)

def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("")
        else:
            form = ReceiptForm()
        return render(request,"/",{"form":form})     

def update_receipt(request,receipt_id):
    context = {}
    receipt_obj = Reciepts.objects.get(id=receipt_id)
    form = ReceiptForm(instance=receipt_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("")
    context['form'] = form
    return render(request,"/",context)

def delete_receipt(request,receipt_id):
    context = {}
    receipt_obj = get_object_or_404(Reciepts,id=receipt_id)
    if request.method == "POST":
        receipt_obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"/",context=context)
