def dfs(graph, start_node):
  ## deque 패키지 임포트
  from collections import deque
  
  visited = []
  need_visited = deque()
  
  # 시작 노드 설정
  need_visited.append(start_node)
  
  # 방문이 필요한 리스트가 존재한다면
  while need_visited:
    # 시작 노드 지정
    node = need_visited.pop()
    
    # 방문한 리스트에 없다면
    if node not in visited:
      # 방문 리스트에 노드 추가
      visited.append(node)
      # 인접한 노드들을 방문 예정 리스트에 추가
      need_visited.extend(graph[node])
      
  return visited