import math
class sphere:
    def _init_(self,radius):
        self.radius = radius
    def diameter(self):
        return 2*r
    def circumference(self):
        return 2 * math.pi *r
    def volume(self):
        return (4/3)*math.pi*r**3
s=sphere()
r=int(input("Enter Radius Of Sphere : "))

print("\nDiameter Of Sphere =",s.diameter())
print("\nCircumference Of Sphere =",s.circumference())
print("\nVolume Of Sphere =",s.volume())
