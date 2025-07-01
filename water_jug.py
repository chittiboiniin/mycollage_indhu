
def water_jug_problem(a,b,target):
    if target > max(a,b):
        print("target is greater than capacity of jug1 & jug2")
    visited=set()
    queue=[(0,0)]
    while queue:
        jug1,jug2=queue.pop(0)
        if jug1==target or jug2==target:
            return True
        possible_states= [
            (a,jug2),
            (jug1,b),
            (0,jug2),
            (jug1,0),
            (jug1-min(jug1,b-jug2),jug2+min(jug1,b-jug2)),
            (jug1+min(jug2,a-jug1),jug2-min(jug2,a-jug1))
            ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False
a=5
b=3
target=12
if water_jug_problem(a,b,target):
    print("Target is achivable")
else:
    print("Target not achivable")
            
