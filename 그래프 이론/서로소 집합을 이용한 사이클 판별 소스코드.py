def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

cycle = False #사이클 발생 여부
for _ in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b): #사이클 발생한 경우 종료
    cycle = True
    break
  else: #사이클이 발생하지 않았다면 합집합(union) 수행
    union_parent(parent, a, b)

if cycle:
  print("사이클이 발생했습니다.")
else:
  print("사이클이 발생하지 않았습니다.")
