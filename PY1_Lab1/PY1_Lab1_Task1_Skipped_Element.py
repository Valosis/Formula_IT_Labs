numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

indexEmptyElem = 0

#Let's find the None element, assuming it exists and it is the only one
for i in range(len(numbers)):
    if numbers[i] is None:
        indexEmptyElem = i
        break

newElem = (sum(numbers[:indexEmptyElem])+sum(numbers[indexEmptyElem+1:]))/len(numbers)
numbers[indexEmptyElem] = newElem

print("Измененный список:", numbers)