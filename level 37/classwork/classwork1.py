#1, Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".
#Print the entire list.
#Access and print the first and last items in the list.
#Add a new fruit "fig" to the list.
#Remove "banana" from the list.
#Change the value of the second item to "blueberry".
#Print the length of the list.


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits +=['fig']

fruits.remove("banana")
fruits.insert(1, 'blueberry')

print(fruits)

print(len(fruits))
