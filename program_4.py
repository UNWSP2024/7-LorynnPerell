# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math

def distance(coord1, coord2):
    return math.sqrt(
        (coord2[0] - coord1[0]) ** 2 +
        (coord2[1] - coord1[1]) ** 2 +
        (coord2[2] - coord1[2]) ** 2
    )

def get_tuple_input(prompt):
    while True:
        try:
            values = input(prompt).split(',')
            if len(values) != 3:
                raise ValueError("You must enter exactly 3 values.")
            x, y, z = map(float, values)
            return (x, y, z)
        except ValueError as e:
            print("Invalid input:", e)

# Mainline
print("Enter two 3D coordinates (e.g., 1,2,3)")

coord1 = get_tuple_input("Enter first coordinate: ")
coord2 = get_tuple_input("Enter second coordinate: ")

dist = distance(coord1, coord2)
print(f"Distance between points: {dist:.2f}")
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 