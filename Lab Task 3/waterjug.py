def waterJugDFS(capacity1, capacity2, target):
    stack = [(0, 0)]  
    visited = set()   
    path = []         
    while stack:
        jug1, jug2 = stack.pop()  
        path.append((jug1, jug2))  
        if jug1 == target or jug2 == target:
            print("\n Solution occurs ! steps in this code are as follows....................:")
            for step in path:
                print(step)
            return True
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        next_states = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),  
            (jug1, 0),  
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   
        ]
        for state in next_states:
            if state not in visited:
                stack.append(state)
    print("\n No Solution Found!")

jug1Capacity = 2
jug2Capacity = 5
target = 2          

waterJugDFS(jug1Capacity, jug2Capacity, target)
