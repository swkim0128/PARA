---
type: Algorithm
archive: false
---
**DFS(Depth First Search)**

깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.

1 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.  
2 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.  
3 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.  

```Python
# DFS 예제

# DFS 메서드 정의
# 재귀 함수 이용.
def dfs(graph, v, visited):
	  # 현재 노드를 방문 처리
		visited[v] = True
		print(v, end=' ')
	    
	  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	  for i in graph[v]:
		    if not visited[i]:
			      dfs(graph, i, visited)
```

```Python
# DFS 예제

# 스택을 이용하여 DFS 구현
def dfs(graph, start, visited):
		# 스택 초기화
		stack = []
		
		# 현재 노드 방문 처리
		visited[start] = True

		# 스택이 빌 때까지 반복
		while stack:
				# 스택에서 하나의 원소를 뽑아 출력
				v = stack.pop()
				print(v, end=' ')

				# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 스택에 삽입
				for i in graph[v]:
						if not visited[i]:
								stack.append(i)
								visited[i] = True
```

**BFS(Breadth First Search)**

너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘.

1 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.  
2 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.  
3 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.  

```Python
# BFS 예제
from collection import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```