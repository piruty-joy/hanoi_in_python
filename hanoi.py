# -*- coding: utf-8 -*-

total_hanoi = 0

def hanoi(n, x, y, z):
  if n == 0: 
    return
  hanoi(n-1, x, z, y)
  global total_hanoi
  total_hanoi = total_hanoi + 1
  print('%s -> %s %d' % (x, y, total_hanoi))
  hanoi(n-1, z, y, x)

if __name__ == '__main__':
  hanoi(10, 'A', 'B', 'C')
