from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, item):
    if isinstance(item, dict):
        quantity = sum(item['items_by_size'].values())
    else:
        quantity = item
    return price * quantity