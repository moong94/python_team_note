class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    answer = ''
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i - 1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i - 1]
    
    stack = []
    curr = nodeArr[k]
    
    for i in cmd:
        if i[0] == "D":
            x = int(i[2:])
            for _ in range(x):
                curr = curr.next
        if i[0] == "U":
            x = int(i[2:])
            for _ in range(x):
                curr = curr.prev
        if i[0] == "C":
            stack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        if i[0] == "Z":
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node
    for i in range(n):
        if nodeArr[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer