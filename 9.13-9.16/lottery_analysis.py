lottery_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = []
winning_ticket = [9, 10, 2, 'c']
count = 0

while my_ticket != winning_ticket:
    my_ticket = []
    for i in range(4):
        from random import choice

        my_ticket.append(choice(lottery_ticket))
        count += 1
    print(str(my_ticket) + " successfully rolled! Count: " + str(count))
