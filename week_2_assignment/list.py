my_list = []
elements_to_append = [10, 20, 30, 40]
my_list.extend(elements_to_append)
print(my_list)
my_list[1] = 15
other_list = [50, 60, 70]
my_list.extend(other_list)
print(my_list)
del my_list[-1]
print(my_list)
my_list.sort()
print(my_list)
print(my_list.index(30))