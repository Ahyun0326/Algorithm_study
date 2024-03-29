from collections import deque

v, e = map(int, input().split())

#진입 차수 0으로 초기화
indegree = [0] * (v + 1)

#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

#방향 그래프 정보 입력 받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  #진입차수 1 증가
  indegree[b] += 1


#위상 정렬 함수
def topology_sort():
  result = []  #수행 결과를 담을 리스트
  q = deque()  #큐 기능을 위한 deque 라이브러리 사용

  #진입 차수가 0인 노드 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  #큐가 빌 때까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)

    #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1

      #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  #위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end=' ')


topology_sort()v
