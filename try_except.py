list1 = [1,2,3,4,5,6,7,8,9,10]
def get_even(li):
  even_list = []
  for num in li:
    if (num % 2) == 0:
      even_list.append(num)
  return even_list

print (get_even(list1))
