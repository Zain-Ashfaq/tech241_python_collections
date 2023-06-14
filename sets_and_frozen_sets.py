# Sets and frozen sets

# {} - list but unordered

car_parts = {"wheels","windows", "exhaust","steering wheel"}
print(car_parts)

# add to a set

car_parts.add("doors")

print(car_parts)

# remove from a set
car_parts.remove("doors")

# frozen set
x = frozenset(["one","two","three"])
print(x)
