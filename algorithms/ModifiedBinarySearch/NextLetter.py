# modified binary search


# Time complexity O(logN) and Space complexity O(1)
def search_next_letter(letters, key):

    start = 0
    end = len(letters)
    last_index = 0

    while start < end:
        mid = (start + end) // 2
        if key < letters[mid]:
            end = mid
            last_index = mid
        elif key > letters[mid]:
            start = mid + 1
        elif key == letters[mid]:
            index = ((mid + 1) % len(letters))
            return letters[index]

    if last_index != 0:
        return letters[last_index]

    return letters[0]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'k'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'a'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'c'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'g'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'd'))



main()
