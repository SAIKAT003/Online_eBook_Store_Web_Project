from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(Books , cart):
    keys=cart.keys()
    for id in keys:
        if id == str(Books.id):
            return True
    return False

@register.filter(name='user_in_cart')
def user_in_cart(user , cart):
    keys=cart.keys()
    for id in keys:
        if id == str(user.id):
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(Books,cart):
    keys=cart.keys()
    for id in keys:
        if id == str(Books.id):
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(Books,cart):
    return Books.price * cart_quantity(Books,cart)

@register.filter(name='price')
def price(Books):
    return Books.price

@register.filter(name='total_cart_price')
def total_cart_price(books,cart):
    sum=0
    for p in books:
        sum+=price_total(p,cart)
    return sum