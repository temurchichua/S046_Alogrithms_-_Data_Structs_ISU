def nextGreatestLetter(letters,  target: str) -> str:
    if target == 'z':
        return letters[0]

    low, high = 0, len(letters) - 1

    while low <= high:
        middle = (low + high) // 2
        print(low, high, middle)
        if letters[middle] <= target:
            low = middle + 1
        else:
            high = middle - 1

    while low + 1 < len(letters) and letters[low] == letters[low + 1]:
        low += 1

    return letters[low]


if __name__ == '__main__':
    letters = ["x","x","y","y"]
    target = "z"
    print(nextGreatestLetter(letters, target))
