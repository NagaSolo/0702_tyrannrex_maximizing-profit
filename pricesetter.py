
# More than 1 customer -> etc customer1, customer2, customer3, .. customerN
# Each has their own budget -> customer1_budget, customer2_budget, customer3_budget, .. customerN_budget
# if declared_price <= customer_budget then buy, else not buy
# declared_price must be price that brings the most revenue
# greedy approach algorithm to set declared_price

# calculate all maximum price for each budget
def get_maximum_price_for_each(list_of_sorted_budget):
    for index, budget in enumerate(list_of_sorted_budget[1:-2]):
        if budget <= next(budget):
            return budget*(range(list_of_sorted_budget[1:-2] - )
            
def get_profit_from_minimum_budget(list_of_sorted_budget):
    return min(list_of_sorted_budget)*len(list_of_sorted_budget)

def get_profit_from_maximum_budget(list_of_sorted_budget):
    return max(list_of_sorted_budget)*len(list_of_sorted_budget)

N = int(input())
customer_budget_list = []
for customer_budget in range(N):
    customer_budget_list.append(int(input()))

customer_budget_list.sort() # sort list inplace
print(customer_budget_list)

get_maximum_price_for_each(customer_budget_list)

# # pseudo case for minimum value
# print(min(customer_budget_list)*len(customer_budget_list))

# # pseudo case for maximum value
# print(max(customer_budget_list))

# pseudo case for in between value
"""
    a = [n, n+1, n+2, n+3 ... n+n]
    min = a[n]
    max = a[n+n]
    if a[n+1] == min; a[n+1]*len(a)
    if a[n+1] != min; a[n+1]*(len(a)-n) 

"""
