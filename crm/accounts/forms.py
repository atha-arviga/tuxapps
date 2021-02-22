from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # mengambil semua field di class Order di model
        fields = '__all__'
        # jika mau hanya field tertentu saja bisa pake dictonary
        # seperti
        # fields = ['customer'.'product']

