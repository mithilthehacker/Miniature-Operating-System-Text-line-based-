
def calc():
  A = "a"
  m = "m"
  s = "s"
  d = "d"
  Num_i = float(input("Enter No. 1 "))
  Num_ii = float(input("Enter No.2 "))
  OPERATOR = input("Operator?(A,S,M,D)")
  if OPERATOR == A:
    print(Num_i + Num_ii)
  elif OPERATOR == s:
    print(Num_i - Num_ii)
  elif OPERATOR == m:
    print(Num_i * Num_ii)
  elif OPERATOR == d:
    print(Num_i / Num_ii)
calc()
