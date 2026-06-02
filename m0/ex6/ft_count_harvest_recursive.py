def	recursion_helper(days, i):
	if (i != days + 1):
		print(f"Day {i}")
		i += 1
		recursion_helper(days, i)
	else:
		print("Harvest time!")

def	ft_count_harvest_recursive():
	i = 1;
	days = int(input("Days until harvest: "))
	recursion_helper(days, i)