
def linear_search(list, target):
    """
    Return the index position of the target if found, else return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


def main():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    target = int(input("Pick a number between 1-30. "))
    result = linear_search(numbers, target)
    verify(result)

if __name__=="__main__":
    main()
    