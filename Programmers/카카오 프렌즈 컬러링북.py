from collections import deque
m,n=map(int,input().split())
visited = [[0 for _ in range(100)] for _ in range(100)]
picture =[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(pixel,y,x):
    cnt=0
    q=deque()
    q.append((y,x))
    while q:
        fy,fx=q.popleft()
        for i in range(4):
            gy,gx=fy+dy[i],fx+dx[i]
            if 0<=gy<m and 0<=gx<n:
                if picture[gy][gx]==pixel and visited[gy][gx]!=1:
                    cnt+=1
                    visited[gy][gx]=1
                    q.append((gy,gx))
    return cnt
def solution(m,n,picture):
    number_of_area=0
    max_size_of_one_area=0
    take=[]
    for i in range(m):
        for j in range(n):
            if visited[i][j]!=1 and picture[i][j]!=0:
                max_size_of_one_area=max(bfs(picture[i][j],i,j),max_size_of_one_area)
                number_of_area+=1
    return number_of_area,max_size_of_one_area
print(solution(m,n,picture))
