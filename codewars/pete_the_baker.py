def cakes(recipe, available):
	max_cakes_4_pete = float("inf")

	# if the ingredient is not available return 0
	for item in recipe:
		if item not in available:
			return 0

	# if the ingredient is available divide what's available by
	# the recipe and update if we get a smaller quotient
	for ingredient in recipe:
		if available[ingredient] / recipe[ingredient] < max_cakes_4_pete:
			max_cakes_4_pete = available[ingredient] / recipe[ingredient]

	return max_cakes_4_pete
