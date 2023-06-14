# Lists and Tuples

# making a list in Python

# shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
#
# print(type(shopping_list))
# print(shopping_list)
#
# # accessing certain parts of list
#
# # print(shopping_list[-1])
#
# # change a specific element of list
#
# shopping_list[4] = "orange juice"
#
# print(shopping_list)
#
# # list methods
#
# shopping_list.append("butter")
# print(shopping_list)
#
# # remove methods
# shopping_list.remove("butter")
# print(shopping_list)
#
# shopping_list.pop()
# print(shopping_list)
#
# x=shopping_list.pop(0)
# print(x)
# print(shopping_list)

# mixed data type list

mixture = [1,2,3,"one","two","three"]
print(mixture)

# list slicing

x = mixture[1:3]
print(x)

# Tuples

# () - Tuples are immutable, as they cannot change

essentials = ("bread","eggs", "milk")
print(essentials)
print(essentials.count("bread"))
