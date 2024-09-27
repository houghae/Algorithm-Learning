
def merge_sort(values):
    """
    Merge sort algorithm, divide and conquer posterchild
    
    Take an unsorted list, recursively separate values in the call stack until base case is reached.
    Then sort and merge the individual values together into a new list.  
    """
    # Base case
    if len(values) <= 1:
        return values
    # Find middle with floor divide operator
    middle_index = len(values) // 2
    # Recursively sort the lists until all lists are of length 1. 
    # These are added to the call stack until the last base case is reached. 
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    # Then it breaks out of the if conditional and moves onto the code below.
    
    # Create an empty list to hold sorted values.
    sorted_values = []
    # Create two variables to keep track of the position of iteration through the left and right values.
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    # This ensures any remaining values are copied over to the sorted list.
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

unsorted_values = [3,11,77,44,21,150,100003,765432,34,67,6,5]


def main():
    print(unsorted_values)
    sorted_values = merge_sort(unsorted_values)
    print(sorted_values)




if __name__=="__main__":
    main()
