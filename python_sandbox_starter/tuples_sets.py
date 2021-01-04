# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value needs trailing comma to be tuple or else is str
fruits2 = ("Apples",)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = "Pears"

# Can't delete tuple
# del fruits[2]

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grapes")

# Add duplicate (doesn't work on set)
fruits_set.add("Apples")

# Remove from set
fruits_set.remove("Grapes")

# Clear set
# fruits_set.clear()

# Delete set
# del fruits_set

print(fruits_set)