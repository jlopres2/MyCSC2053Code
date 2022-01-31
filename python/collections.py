# PRACTICE CODE

# tuples (can't change them)
coordinates = (5, 25)
print(coordinates)
x, y = coordinates
print(x,y)
print(coordinates[0])

# sets
set1 = {1,2,3,3,2}
print(set1)
list1 = [1,2,2,3,3,4,4]
list_remove_dups = set(list1)
print(list_remove_dups)

# comprehension
list1 = []
for i in range(0,50):
    list1.append(i)
print(list1)
list2 = [x for x in range(0, 50)] # this does the same thing
print(list2)
list3 = [x for x in range(0, 50) if x > 40]
print(list3)
list_even = [x for x in range(0, 50) if x % 2 == 0]
print(list_even)
list_odd = [x for x in range(0, 50) if x % 2 != 0]
print(list_odd)

# dictionary
favorite_foods = {"Kathleen": "pizza", "Steve": "burgers", "John": "chicken"}
favorite_foods["Michelle"] = "pasta"
favorite_foods["Patrick"] = "cookies"
print(favorite_foods)

for key, value in favorite_foods.items():
    print(key + "'s favorite food is " + value)
if "Mary" in favorite_foods:
    print("Mary in dictionary")
else:
    favorite_foods["Mary"] = "cake"

# counting in the dictionary
foods = ["pizza", "tikka masala", "pizza", "bagels", "bagels", "ice cream", "pizza"]
food_count = {}
for num in foods: # this can be done in one line with comprehension
    if num not in food_count:
        food_count[num] = 1
    else:
        food_count[num] += 1
print(food_count)

# comprehension/dictionary
keys = ["one","two","three"]
nums = {keys[i]: i + 1 for i in range(len(keys))}
print(nums)



