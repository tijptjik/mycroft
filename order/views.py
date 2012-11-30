from coffin.shortcuts import render, get_object_or_404

from models import UnawareOrder


def show_order(request, order_id):
    order = get_object_or_404(UnawareOrder, id=order_id)
    return render(
        request,
        'order/show_order.html',
        {'order': order}
    )
