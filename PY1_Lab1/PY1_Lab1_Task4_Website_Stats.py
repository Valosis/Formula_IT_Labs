usersList = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# Step 1
dictUsers = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

# Step 2
dictUsers["Общее количество"] = len(usersList)

# Step 3
setUsers = set(usersList)
dictUsers["Уникальные посещения"] = len(setUsers)

# Step 4
print(dictUsers)