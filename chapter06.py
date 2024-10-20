#OBJECT REFERENCES, MUTABILITY, AND RECYCLING
### Exercise 1: Understanding Object References

#**Task**: Create a list `a` and assign it to another variable `b`. Modify the list through `b` and observe the changes through `a`.
#**Example Solution**:
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Output: [1, 2, 3, 4]

#**Explanation**: Both `a` and `b` reference the same list object, so changes through `b` are reflected in `a`.


### Exercise 2: Working with Immutable Tuples
#**Task**: Create a tuple `t1` and make a shallow copy using slicing. Verify if they reference the same object.
#**Example Solution**:
t1 = (1, 2, 3)
t2 = t1[:]
print(t2 is t1)  # Output: True

#**Explanation**: Slicing a tuple does not create a new object but returns a reference to the same object.


### Exercise 3: Aliasing and Mutability
#**Task**: Create a list `l1` containing another list. Make a shallow copy of `l1` and modify the nested list through the copy. Observe the changes in the original list.
#**Example Solution**:
l1 = [1, [2, 3], 4]
l2 = list(l1)
l2[1].append(5)
print(l1)  # Output: [1, [2, 3, 5], 4]

#**Explanation**: The nested list `[2, 3]` is shared between `l1` and `l2`, so changes through `l2` affect `l1`.


### Exercise 4: Deep Copying
#**Task**: Create a nested list and make a deep copy using the `copy` module. Modify the nested list in the copy and verify that the original list remains unchanged.
#**Example Solution**:
import copy
l1 = [1, [2, 3], 4]
l2 = copy.deepcopy(l1)
l2[1].append(5)
print(l1)  # Output: [1, [2, 3], 4]
print(l2)  # Output: [1, [2, 3, 5], 4]

#**Explanation**: `deepcopy` creates a completely independent copy, so changes in `l2` do not affect `l1`.


### Exercise 5: Function Parameters and Mutability
#**Task**: Write a function that modifies a list passed as a parameter. Call the function and observe the changes in the original list.
#**Example Solution**:
def modify_list(lst):
    lst.append(4)

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)  # Output: [1, 2, 3, 4]

#**Explanation**: The list `original_list` is passed by reference, so the function modifies the original object.




#INTRODUCING LISTS

### Exercises
#Here are three exercises that tie these concepts together:
### Exercise 1: Manage a List of Guests
#**Task:**
#1. Create a list of guests to invite to a party.
#2. Print an invitation message for each guest.
#3. One guest can't make it; replace that guest with a new one.
#4. Add three more guests to the list and print new invitations.
#5. Remove guests one by one until only two remain, apologizing to each removed guest.
#**Example Solution:**

# Step 1: Create a list of guests
guests = ['Alice', 'Bob', 'Charlie']
print(guests)

# Step 2: Print invitation messages
for guest in guests:
    print(f"Dear {guest}, you are invited to my party!")

# Step 3: Replace a guest
print("\\nCharlie can't make it.")
guests[2] = 'David'
for guest in guests:
    print(f"Dear {guest}, you are invited to my party!")

# Step 4: Add more guests
print("\\nFound a bigger table!")
guests.insert(0, 'Eve')
guests.insert(2, 'Frank')
guests.append('Grace')
for guest in guests:
    print(f"Dear {guest}, you are invited to my party!")

# Step 5: Remove guests until only two remain
print("\\nSorry, I can only invite two guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to the party.")
for guest in guests:
    print(f"Dear {guest}, you are still invited to my party!")

# Remove the last two guests and check the empty list
del guests[0]
del guests[0]
print(guests)  # Should print an empty list



### Exercise 2: Organize a List of Locations
#**Task:**
#1. Create a list of places you'd like to visit.
#2. Print the list in its original order.
#3. Print the list in alphabetical order without modifying the original list.
#4. Print the list in reverse-alphabetical order without modifying the original list.
#5. Reverse the order of the list.
#6. Sort the list in alphabetical and then in reverse-alphabetical order.
#**Example Solution:**

# Step 1: Create a list of places to visit
places = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Rome']

# Step 2: Print original list
print("Original list:", places)

# Step 3: Print alphabetical order
print("Alphabetical order:", sorted(places))

# Step 4: Print reverse-alphabetical order
print("Reverse-alphabetical order:", sorted(places, reverse=True))

# Step 5: Reverse the list
places.reverse()
print("Reversed list:", places)

# Step 6: Sort the list alphabetically and then reverse-alphabetically
places.sort()
print("Sorted list:", places)
places.sort(reverse=True)
print("Reverse-sorted list:", places)



### Exercise 3: Manage a List of Motorcycles
#**Task:**
#1. Create a list of motorcycles and print it.
#2. Modify the first element and print the list.
#3. Add a motorcycle to the end of the list and print it.
#4. Insert a motorcycle at the beginning of the list and print it.
#5. Remove the second motorcycle using `del` and print the list.
#6. Pop the last motorcycle and print the list and the popped value.
#**Example Solution:**

# Step 1: Create a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Original list:", motorcycles)

# Step 2: Modify the first element
motorcycles[0] = 'ducati'
print("Modified list:", motorcycles)

# Step 3: Append a motorcycle
motorcycles.append('harley')
print("Appended list:", motorcycles)

# Step 4: Insert a motorcycle at the beginning
motorcycles.insert(0, 'bmw')
print("List after insertion:", motorcycles)

# Step 5: Remove the second motorcycle using del
del motorcycles[1]
print("List after deletion:", motorcycles)

# Step 6: Pop the last motorcycle
popped_motorcycle = motorcycles.pop()
print("List after popping:", motorcycles)
print("Popped motorcycle:", popped_motorcycle)

#These exercises help solidify the understanding of list operations, including creating, modifying, organizing, and managing lists in Python.




#WORKING WITH LISTS

### Exercises with Examples
#1. **Exercise: Modifying Guest List**
#**Task**: Start with a list of guests you'd like to invite to dinner. Replace a guest who can't make it with someone else.
#*Example**:

guests = ['Alice', 'Bob', 'Charlie']
print(f"Original guests: {guests}")
        
# Bob can't make it
print("Bob can't make it to the dinner.")
guests[1] = 'David'
        
# Print new invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
        
        
#2. **Exercise: Adding and Removing Items**
#Task**: Create a list of your favorite foods, add new foods to the list, and remove a food item.
#Example**:
        
favorite_foods = ['pizza', 'sushi', 'tacos']
print(f"Original list: {favorite_foods}")
        
# Adding foods
favorite_foods.append('pasta')
favorite_foods.insert(1, 'burger')
print(f"List after adding foods: {favorite_foods}")
        
# Removing a food item
favorite_foods.remove('sushi')
print(f"List after removing a food item: {favorite_foods}")
        
#3. **Exercise: Working with Tuples**
#Task**: Define a tuple with dimensions of a rectangle, print the dimensions, then redefine the tuple and print the new dimensions.
#Example**:      
        
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
        
# Redefine the tuple
dimensions = (400, 100)
print("\\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

