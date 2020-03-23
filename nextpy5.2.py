'''
5.2.3
You have in your wallet 3 bills of 20, 5 bills of 10, 2 bills of 5, and 5 bills of 1
calculate all permutations which total to $100 and print them to the screen
count the number of permutations
'''

from itertools import combinations

wallet = {1: 5, 5: 2, 10: 5, 20: 3}  # bill value: amount
bills = []
for k, v in wallet.items():
    for i in range(v):
        bills.append(k)
print(bills)
combs = []
for j in range(len(bills)):
    for comb in combinations(bills, j):
        if sum(comb) == 100 and tuple(sorted(comb)) not in combs:
            combs.append(comb)
print(combs)
print(len(combs))
