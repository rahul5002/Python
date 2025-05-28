class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

P1 = Point(10, 20)
P2 = Point(12, 15)

P3 = P1 + P2

print("P1:", P1)
print("P2:", P2)
print("P3 = P1 + P2:", P3)