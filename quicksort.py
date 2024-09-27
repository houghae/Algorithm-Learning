def quicksort(values):
  """
  Recursive sorting algorithm that iterates though a list starting at the beginning.
  """
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


random_list = [3,11,77,44,21,150,100003,765432,34,67,6,5]


def main():
  print(random_list)
  sorted_list = quicksort(random_list)
  print(sorted_list)


if __name__=="__main__":
  main()