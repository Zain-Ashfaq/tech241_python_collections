# Collections
A collection is a way to store and work with groups of data conveniently. It provides specialized structures and modules that make it easier to handle and manipulate multiple objects together.

# Lists and Tuples
To create a list in Python, you can assign multiple values to a variable using square brackets [] and separating the elements with commas. Here's an example:

```python
shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
```
## Accessing List Elements

You can access specific elements in a list using indexing. The index starts at 0 for the first element, -1 for the last element, and so on. For example, shopping_list[0] gives you the first item in the list.
Modifying a List

Lists are mutable, meaning you can change their elements. You can assign a new value to a specific index to modify an element. For instance, shopping_list[4] = "orange juice" replaces the fifth element with "orange juice".
List Methods

Lists have built-in methods to perform various operations. Here are a few examples:

    append(): Adds an element to the end of the list.
    remove(): Removes the first occurrence of a specific element.
    pop(): Removes and returns the last element by default, or a specified index.

## Mixed Data Type List

Lists in Python can contain elements of different data types. For example, you can have a list with integers and strings together:

```python
mixture = [1, 2, 3, "one", "two", "three"]
```
## List Slicing

You can extract a sublist, or a slice, from a list using the slicing notation. For example, x = mixture[1:3] retrieves elements at index 1 and 2.
Tuples

Tuples are similar to lists but are immutable, meaning they cannot be modified after creation. Tuples are defined using parentheses (). Here's an example:

```python
essentials = ("bread", "eggs", "milk")
```
You can access elements and use some methods with tuples just like with lists. For example, essentials.count("bread") returns the number of occurrences of "bread" in the tuple.

## Dictionaries

A dictionary is a data structure in Python that stores data in key-value pairs. It allows you to associate a value with a unique key, enabling efficient retrieval and manipulation of data based on the key.
Making a Dictionary

To create a dictionary in Python, you can enclose key-value pairs within curly braces {}. Each key-value pair is separated by a colon :. Here's an example:

```python

student_1 = {
    "name": "zain",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"]
}
```
## Accessing Dictionary Elements

You can access specific values in a dictionary by using the corresponding key. For example, student_1["name"] retrieves the value associated with the key "name".

```python

print(student_1["name"])
print(student_1["completed_lesson_names"][:1])
```
## Changing a Value

Dictionaries are mutable, so you can modify the value of a specific key. For instance, student_1["completed_lessons"] = 3 changes the value of the "completed_lessons" key to 3.

```python

student_1["completed_lessons"] = 3
print(student_1)
```
## Modifying Dictionary Values

If a dictionary value is mutable, such as a list, you can modify it directly. For example, student_1["completed_lesson_names"].remove("data_types") removes "data_types" from the list of "completed_lesson_names".

```python

student_1["completed_lesson_names"].remove("data_types")
print(student_1)
```
## Dictionary Methods

Dictionaries have built-in methods to perform various operations. Here are a couple of examples:

```python

print(student_1.keys())
print(student_1.values())
```
The keys() method returns a list of all the keys in the dictionary, and the values() method returns a list of all the values.

## Sets and Frozen Sets

Sets are unordered collections of unique elements in Python. They are defined using curly braces {} and can contain various types of elements such as numbers, strings, or even other sets. Sets are mutable, meaning that their elements can be added or removed.

Here's an example of creating a set and printing its contents:

```python

car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts)
```
The elements are printed in an arbitrary order since sets do not maintain any specific order.
Adding Elements to a Set

To add an element to a set, you can use the add() method. It takes a single argument representing the element to be added. Here's an example:

```python

car_parts.add("doors")
print(car_parts)
```
The new element "doors" has been added to the set.
Removing Elements from a Set

To remove an element from a set, you can use the remove() method. It takes a single argument representing the element to be removed. Here's an example:

```python

car_parts.remove("doors")
print(car_parts)
```
The element "doors" has been successfully removed from the set.
Frozen Sets

Frozen sets, on the other hand, are immutable sets. Once created, their elements cannot be modified. They are defined using the frozenset() function and take an iterable as an argument. Here's an example:

```python

x = frozenset(["one", "two", "three"])
print(x)
```
The elements of a frozen set are also printed in an arbitrary order. Being immutable, frozen sets do not have methods like add() or remove() since their elements cannot be modified once created.
