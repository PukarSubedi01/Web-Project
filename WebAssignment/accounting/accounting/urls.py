"""accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application.views import billView,customerView,signupView,vendorView,invoiceView,views

urlpatterns = [
    path('vendors', vendorView.vendors),
    path('edit/vendor/<int:id>', vendorView.edit_vendor),
    path('update/vendor/<int:id>', vendorView.update_vendor),
    path('delete/vendor/<int:id>',vendorView.delete_vendor),
    path('addvendor', vendorView.addvendor),

    path('customers', customerView.customers),
    path('addcustomer', customerView.addcustomer),
    path('edit/customer/<int:id>', customerView.editCustomers),
    path('update/customer/<int:id>', customerView.update_customer),
    path('delete/customer/<int:id>', customerView.delete_customer),

    path('signup', signupView.signup),

    path('invoices', invoiceView.invoices),
    path('invoice/create', invoiceView.newInvoice),
    path('delete/invoice/<int:id>', invoiceView.delete_invoice),
    path('edit/invoice/<int:id>', invoiceView.edit_invoice),
    path('update/invoice/<int:id>', invoiceView.update_invoice),

    path('items/create', views.newItem),

    path('bills', billView.bills),
    path('bills/create', billView.newbill),
    path('delete/bill/<int:id>', billView.delete_bill),
    path('edit/bill/<int:id>', billView.edit_bill),
    path('update/bill/<int:id>', billView.update_bill),

    path('dashboard', views.dashboard),

    path('items', views.items),




    path('admin/', admin.site.urls),
    path('index', views.index),
    path('entry', views.entry)

]
