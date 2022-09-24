lottery_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("the winning lottery ticket is: ")
for i in range(4):
    from random import choice
    print(choice(lottery_ticket))

