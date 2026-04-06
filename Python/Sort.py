def insert_sorted():
    sortList = []
    print("Enter number :")

    while True:
        val = int(input("> "))
        if val == 0:
            break

        flag = False
        for i in range(len(sortList)):
            if val < sortList[i]:
                sortList.insert(i, val)
                flag = True
                break

        if not flag:
            sortList.append(val)

        print(f"Current list: {sortList}")

insert_sorted()