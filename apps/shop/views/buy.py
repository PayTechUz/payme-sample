from django.db import transaction
from django.shortcuts import render
from django.shortcuts import redirect

from shop.models import Product
from shop.models import CustomOrderModel

from payme.models import Item
from payme.models import OrderDetail
from payme.models import ShippingDetail
from payme.methods.generate_link import GeneratePayLink


def buy_view(request, pk):
    product = Product.objects.get(pk=pk)

    if request.POST:
        full_name = request.POST.get('fullname')
        phone_number = request.POST.get('number')
        wants_at = request.POST.get('date')
        count = request.POST.get('how_much')
        address = request.POST.get('address')

        fields = [full_name, phone_number, wants_at, count, address]

        for field in fields:
            if field is None or "":
                return False
  
        with transaction.atomic():
            item = Item.objects.get(pk=pk)
            item.count = count
        
            shipping_detail = ShippingDetail.objects.create(
                title=address,
                price=0
            )

            detail = OrderDetail.objects.create(
                shipping=shipping_detail
            )
            detail.items.add(item)

            order = CustomOrderModel.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                wants_at=wants_at,
                detail=detail
            )

            pay_link = GeneratePayLink(
                order_id=order.id,
                amount=item.price
            ).generate_link()

            return redirect(pay_link)


    context = {
        "product": product
    }   

    return render(request, 'buy_form.html', context)
