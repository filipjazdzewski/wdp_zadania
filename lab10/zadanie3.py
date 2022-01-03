import random
import math

points = [{'x': random.randint(-30, 30), 'y': random.randint(-30, 30)} for i in range(10)]
print(points)

distance = math.sqrt((points[0]['x'] - points[1]['x']) ** 2 + ((points[0]['y'] - points[1]['y']) ** 2))


