
def calculate_discount(price,discount_percent):
    if discount_percent >= 0.2:
        final_amount= price- (discount_percent*price)
        print(final_amount)
    else:
        final_amount=price
        print(final_amount)

a=float(input('Enter the price: '))
b=int(input('Enter the % discount: '))
c= b/100

calculate_discount(a,c)
