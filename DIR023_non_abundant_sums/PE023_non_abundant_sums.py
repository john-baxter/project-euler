from euler.functions import get_list_of_factors

def is_it_abundant_or_not(number):
  if sum(get_list_of_factors(number)) > number:
    return True
  else:
    return False

def find_all_abundant_numbers_below(limit):
  list_of_abundants = []
  for i in range(limit):
    if is_it_abundant_or_not(i):
      list_of_abundants.append(i)
  return list_of_abundants


if __name__ == '__main__':
  # print(is_it_abundant_or_not(28))
  print(find_all_abundant_numbers_below(100))
