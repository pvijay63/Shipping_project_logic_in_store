"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""
X=100
customer_basket_cost = 34
customer_basket_weight = 44
shipping_cost=1.20
customer_total_cost=customer_basket_cost+customer_basket_weight
if(customer_basket_cost>=X):
 print('they get free shipping')
else:
  shipping_cost=customer_basket_weight*shipping_cost
  customer_basket_cost=shipping_cost+customer_basket_cost
  print("The total shipping cost is "+str(customer_basket_cost))