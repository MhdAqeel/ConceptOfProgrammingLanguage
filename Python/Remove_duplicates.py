def remove_duplicates_keep_order(items):
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


if __name__ == "__main__":
    arr = []
    while True:
        n = int(input())
        if n==0:
            break
        arr.append(n)

    print("Original:", arr)
    print("Deduped: ", remove_duplicates_keep_order(arr))
