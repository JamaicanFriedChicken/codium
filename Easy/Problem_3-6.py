"""
n=1		n=2     n=3         n=4
+       A+B     AA+BB       AAA+BBB
        +E+     A+E+B       AA+E+BB
        C+D  	+EEE+       A+EEE+B
                C+E+D       +EEEEE+
                CC+DD       C+EEE+D
                            CC+E+DD
                            CCC+DDD
"""

def sequence(d):
   c, l = 0, 1
   while c < d - 1:
     if l%2:
       yield l
       c += 1
     l += 1

def make_pattern(d):
   t, b, r = f'{"A"*(d-1)}+{"B"*(d-1)}', f'{"C"*(d-1)}+{"D"*(d-1)}', list(sequence(d))
   body = '\n'.join(f'{"A"*((r[-1]-i)//2)}+{"E"*i}+{"B"*((r[-1]-i)//2)}' for i in r[:-1]) + \
     f'\n+{"E"*r[-1]}+\n'+'\n'.join(f'{"C"*((r[-1]-i)//2)}+{"E"*i}+{"D"*((r[-1]-i)//2)}' for i in r[:-1][::-1])
   return f'{t}\n{body}\n{b}'

def diamond(d):
  return {1:lambda _:'+', 2:lambda _:'A+B\n+E+\nC+D'}.get(d, make_pattern)(d)


if __name__ == '__main__':
    print(diamond(1))
    print('-'*5)
    print(diamond(3))
    print('-'*5)
    print(diamond(4))
