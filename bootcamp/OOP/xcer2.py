class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        str_radius = f'radius converted to string is {str(self.radius)}'
        return str_radius

moon = Circle(1737)
print(moon)
    