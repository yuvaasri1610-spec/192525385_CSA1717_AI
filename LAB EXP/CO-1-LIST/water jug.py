from collections import deque

def water_jug(cap1, cap2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        possible_states = [
            (cap1, b),                 # Fill jug 1
            (a, cap2),                 # Fill jug 2
            (0, b),                    # Empty jug 1
            (a, 0),                    # Empty jug 2
            (a - min(a, cap2 - b),
             b + min(a, cap2 - b)),    # Pour jug 1 into jug 2
            (a + min(b, cap1 - a),
             b - min(b, cap1 - a))     # Pour jug 2 into jug 1
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None

cap1 = 4
cap2 = 3
target = 2

path = water_jug(cap1, cap2, target)

if path:
    print("Solution steps:")
    for step, state in enumerate(path):
        print(f"Step {step}: Jug 1 = {state[0]} L, "
              f"Jug 2 = {state[1]} L")
else:
    print("No solution exists.")
