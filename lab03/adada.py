def find_list_recursion(list1, numb):
   if list1 == numb:
      return 0
   elif isinstance(list1, list):
      for index, number in enumerate(list1):
         result = find_list_recursion(number, numb)
         if result is not None:
            return index + result
   return None

def find_list_without_recursion2(list1, numb):
   stack = [(list1, [])]
   while stack:
      current, depth = stack.pop()
      if current == numb:
         return sum(depth)
      if isinstance(current, list):
         for index, item in enumerate(current):
               stack.append((item, depth + [index]))
   return None
def find_number_without_recursion(u, v, k):
   a1, b1 = u, v
   for x in range(2, k+1):
      a1, b1 = 2 * b1 + a1, 2 * b1 * b1 + b1
   return a1, b1

def find_number_with_recursion(a1, b1, k):
   if k == 1:
      return a1, b1
   else:
      new_a = 2 * b1 + a1
      new_b = 2 * b1 * b1 + b1
      return find_number_with_recursion(new_a, new_b, k - 1)

if __name__ == "__main__":
   print(find_list_recursion([1, 2, [3, 4, [5, [6, []]]]], 4))
   print(find_list_recursion([1, 2, [3, 4, [5, [6, []]]]], 'spam'))  

   print(find_list_without_recursion2([1, 2, [3, 4, [5, [6, []]]]], 4))
   print(find_list_without_recursion2([1, 2, [3, 4, [5, [6, []]]]], 'zov'))

   print(find_number_without_recursion(1, 1, 3))
   print(find_number_with_recursion(1, 1, 3))
   