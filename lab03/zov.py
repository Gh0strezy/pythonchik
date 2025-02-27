def findListRecursion(list1, numb):
   if list1 == numb:
      return 0
   elif isinstance(list1, list):
      for index, number in enumerate(list1):
         result = findListRecursion(number, numb)
         if result is not None:
            return index + result
   return None

def findListWithoutRecursion2(list1, numb):
   stack = [(list1, [])]  # Начальный стек: корневой список с глубиной 0
   while stack:
      current, depth = stack.pop()
      if current == numb:
         return sum(depth)
      if isinstance(current, list):
         for index, item in enumerate(current):
               stack.append((item, depth + [index]))  # Увеличиваем глубину для каждого элемента
         
   return None # Если элемент не найден
def findNumberWithoutRecursion(u, v, k):
   a1, b1 = u, v
   for x in range(2, k+1):
      a1, b1 = 2 * b1 + a1, 2 * b1 * b1 + b1
   return a1, b1

def findNumberWithRecursion(u, v, k):
   def recursion(a1, b1, current_k):
      if current_k == k:
         return a1, b1
      else:
         new_a = 2 * b1 + a1
         new_b = 2 * b1 * b1 + b1
         return recursion(new_a, new_b, current_k + 1)
   return recursion(u, v, 1)

if __name__ == "__main__":
   print(findListRecursion([1, 2, [3, 4, [5, [6, []]]]], 5))
   print(findListRecursion([1, 2, [3, 4, [5, [6, []]]]], 'spam'))  

   print(findListWithoutRecursion2([1, 2, [3, 4, [5, [6, []]]]], 5))
   print(findListWithoutRecursion2([1, 2, [3, 4, [5, [6, []]]]], 'zov'))

   print(findNumberWithoutRecursion(1, 1, 3))
   print(findNumberWithRecursion(1, 1, 3))