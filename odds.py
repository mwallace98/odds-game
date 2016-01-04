from random import randint
print(randint(1,13))
def hand(players):
	my_list = []
	for i in range(players):
		my_list.append(randint(1,13))
	return min(my_list)	
hand(2)
my_dict = {1:0, 2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0}
for i in range(100000):
	losing_card = hand(2)
	my_dict[losing_card] += 1
print my_dict[1] / 100000.0	
print my_dict 	