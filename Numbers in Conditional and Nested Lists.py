odd_number_list = [x for x in range(20) if x%2==0] 
print(odd_number_list)

even_number_list = [x for x in range(100) if x%2==0 if x%5==0]
print(even_number_list)

number_lists = [odd_number_list], [even_number_list]
print(number_lists)
