#step 01 take input from user
arr = []
while True:
    n = int(input())
    if n==0:
        break
    arr.append(n)

#step 02 manual sorting
length = len(arr)
for i in range(length):
    for j in range(0,length-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

#print array
print(arr)
    

