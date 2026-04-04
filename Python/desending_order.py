#step 01 take input from the user

arr = []

while True:
    x = int(input())
    if x == 0:
        break
    arr.append(x)

print(arr)

#Step 02 manual sorting

length = len(arr)
for i in range(length):
    for j in range(0,length-i-1):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)