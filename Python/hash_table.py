# Create hash table (10 empty lists)
hash_table = [[] for _ in range(10)]

# Initial values from the exam example
values = [27, 29, 5, 12, 23, 34, 36, 47, 58, 45, 56, 67, 78, 89, 98, 1, 14, 25, 52, 69, 70, 91, 2]

# Insert values into hash table using (number // 10)
for num in values:
    index = num // 10
    hash_table[index].append(num)

# Input search number
search = int(input("Enter number: "))
index = search // 10

# Access the specific bucket
target_list = hash_table[index]

for i in range(10):
    print(f"Bucket {i}: {hash_table[i]}")

# Check-or-insert logic
if search in target_list:
    # Scenario: Number exists
    print(target_list)
else:
    # Scenario: Number doesn't exist - Insert it!
    target_list.append(search)
    print(target_list)