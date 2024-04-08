
def print_type_and_value(var):
  print(f"{var} has a type {type(var)}")

def my_var():
  a = 42
  print_type_and_value(a)

  b = '42'
  print_type_and_value(b)

  c = "quarante-deux"
  print_type_and_value(c)

  d = 42.0
  print_type_and_value(d)

  e = True
  print_type_and_value(e)

  lst = [42]
  print_type_and_value(lst)

  dict = {42 : 42}
  print_type_and_value(dict)

  tuple = (42,)
  print_type_and_value(tuple)

  set = 'set()'
  print_type_and_value(set)

if __name__ == "__main__":
  my_var()


