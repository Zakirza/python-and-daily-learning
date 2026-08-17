def circle(radius:float) -> float:
    """Calculate the area of a circle given its radius."""
    area=3.14*(radius**2)
    print(f"The area of the circle with radius {radius} is {area}")

def rectangle(length:float, breadth:float) -> float:
    """Calculate the area of a rectangle given its length and breadth."""
    area=length*breadth
    print(f"The area of the rectangle with length {length} and breadth {breadth} is {area}")

def triangle(base:float, height:float) -> float:
    """Calculate the area of a triangle given its base and height."""
    area=0.5*base*height
    print(f"The area of the triangle with base {base} and height {height} is {area}")

def square(side:float) -> float:
    """Calculate the area of a square given its side length."""
    area=side**2
    print(f"The area of the square with side {side} is {area}")


if __name__=="__main__":

    circle(5)                   # these four lines only run when the module is executed directly, not when imported
    rectangle(4, 6)
    triangle(3, 7)
    square(4)