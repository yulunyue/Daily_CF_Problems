n, a, b = map(int, input().split())
grid = [[0] * n for _ in range(n)]

if a > 1:
  if b > 1:
    exit(print('NO'))
  else:
    for i in range(n - a + 1):
      for j in range(n - a + 1):
        if i != j:
          grid[i][j] = 1

else:
  if b > 1:
    for i in range(n):
      for j in range(n):
        if i != j:
          grid[i][j] = 1

    for i in range(n - b + 1):
      for j in range(n - b + 1):
        if i != j:
          grid[i][j] = 0
  else:
    if n == 2 or n == 3:
      exit(print('NO'))

    for i in range(n):
      for j in range(n):
        if abs(i - j) == 1:
          grid[i][j] = 1

print('YES')
for x in grid:
  print(''.join(map(str, x)))