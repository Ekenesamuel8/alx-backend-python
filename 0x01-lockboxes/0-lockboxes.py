def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if key < n:
                    stack.append(key)
    
    return len(visited) == n