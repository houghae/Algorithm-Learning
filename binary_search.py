import sys

def iterative_binary(list, target):
    """
    Specify list and target, iteratively search through values.
    Runtime is O(log n) I think, because the slice operation takes O(k) runtime. 
    """
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def recursive_binary(list, target, start=0, end=None):
    """
    Specify a list and target. Recursively search through list.
    Runtime is O(log n). There is no slicing like above.
    Python has a maximum recursion depth and iterative search is still preferred.
    """
    if end is None:
        end = len(list) - 1
    if start > end:
        # Some people use -1 as a placeholder for an index value that doesn't exist.
        # I prefer to have the program exit with a descriptive error comment.
        # return -1
        sys.exit("Target value is not within list")
    
    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary(list, target, start, mid-1)
        else:
            return recursive_binary(list, target, mid+1, end)
        

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


def main():
    numbers = [-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    target = int(input("Pick a number between 1-30. "))
    result = recursive_binary(numbers, target)
    verify(result)

if __name__=="__main__":
    main()
    



