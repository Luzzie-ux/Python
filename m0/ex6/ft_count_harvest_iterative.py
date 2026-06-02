def	ft_count_harvest_iterative():
	i = 1
	days = int(input("Days until harvest: "))
	while (i < days + 1):
		print(f"Day {i}")
		if (i == days):
			print("Harvest time!")
		i += 1
