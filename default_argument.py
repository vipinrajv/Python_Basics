def net_price(mrp,discount=0.10,tax=0.20): # DEFALT VALUES SHOULD COME LATER
    return mrp*(1-discount)*(1+tax)
print(net_price(100))
print(net_price(100,.2,.4))
