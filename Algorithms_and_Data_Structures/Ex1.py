# Time complexity of accessing data in dictionary is O(1) so we changed program from O(n^2) to O(n)
# where n is size of bigger list
def count_connections2(list1: list, list2: list) -> int:
  count = 0
  d = {}
  for i in list2:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  for i in list1:
    count += d[i]
  return count