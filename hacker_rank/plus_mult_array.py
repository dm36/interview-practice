def plusMult(A):
  even = r_even(A)
  odd = r_odd(A)
  if even == odd:
      return "NEUTRAL"
  elif even > odd:
      return "EVEN"
  else:
      return "ODD"


def r_odd(A):
    print A
    mult = True
    result = A[1]
    for i in range(3, len(A), 2):
        # print i, result, mult
        # # first we multiply- and then we set mult to False
        # # so that we add th next round
        if mult:
            result *= A[i]
            mult = False
        else:
            result += A[i]
            mult = True
        print i, result, mult
    return result % 2

def r_even(A):
    print A
    mult = True
    result = A[0]
    for i in range(2, len(A), 2):
        # print i, result, mult
        # # first we multiply- and then we set mult to False
        # # so that we add th next round
        if mult:
            result *= A[i]
            mult = False
        else:
            result += A[i]
            mult = True
    print result
    return result % 2

A = [12, 3, 5, 7, 13, 12]
print plusMult(A)
