
# More than 1 customer -> etc customer1, customer2, customer3, .. customerN
# Each has their own budget -> customer1_budget, customer2_budget, customer3_budget, .. customerN_budget
# if declared_price <= customer_budget then buy, else not buy
# declared_price must be price that brings the most revenue
# greedy approach algorithm to set declared_price

# calculate all maximum price for each budget
def get_maximum_price_for_each(list_of_budget):
    count = 0
    for budget in range(len(list_of_budget) - 1):
        if list_of_budget[budget] <= list_of_budget[budget] + 1:
            count += 1
        # elif list_of_budget[budget] >= list_of_budget[budget] + 1:
        #     count -= 1
        print(count)
    #print(count)
        # list_of_budget[i]*len(list_of_budget)

N = int(input())
customer_budget_list = []
for customer_budget in range(N):
    customer_budget_list.append(int(input()))

customer_budget_list.sort()
print(customer_budget_list)

# pseudo case for minimum value
print(min(customer_budget_list)*len(customer_budget_list))

# pseudo case for maximum value
print(max(customer_budget_list))

# pseudo case for in between value
"""
    a = []
    if a[1] == a[0]; a[1]*len(a)
    if a[1] > a[0]; a[1]*(len(a)-1) 

"""
for i in range(len(customer_budget_list[1:-1])):
    if customer_budget_list[i] <= customer_budget_list[i+1]:
        print(customer_budget_list[i]*len(customer_budget_list[:-1]))
# get_maximum_price_for_each(customer_budget_input)