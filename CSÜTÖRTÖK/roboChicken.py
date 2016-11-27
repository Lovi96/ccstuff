import math
chicken = [0, 0]
while True:
    direction = input("Which direction?")
    step = int(input("How many steps?"))
    if direction == "up":
        chicken[0] += step
    elif direction == "down":
        chicken[0] -= step
    elif direction == "left":
        chicken[1] -= step
    elif direction == "right":
        chicken[1] += step

    distance = math.sqrt((chicken[0])**2 + (chicken[1])**2)
    print(distance)
