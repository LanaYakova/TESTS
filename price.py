def discounted (price, discount, max_discount=50):
    price=abs(float(price))
    discount=abs(float(discount))
    if discount>=max_discount:
        price_with_discount=price
    else:
        price_with_discount=price-price*discount/100
    return price_with_discount

discounted(100, 80)



