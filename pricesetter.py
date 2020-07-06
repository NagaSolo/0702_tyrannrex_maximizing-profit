
# More than 1 customer -> etc customer1, customer2, customer3, .. customerN
# Each has their own budget -> customer1_budget, customer2_budget, customer3_budget, .. customerN_budget
# if declared_price <= customer_budget then buy, else not buy
# declared_price must be price that brings the most revenue
# greedy approach algorithm to set declared_price

N = int(input())
for customer_budget in range(N):
    customer_budget_input = int(input())