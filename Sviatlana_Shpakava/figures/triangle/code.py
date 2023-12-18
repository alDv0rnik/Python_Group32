a = 7
b = 2
c = 8

def triangle_perimeter(side_x=a, side_y=b, side_z=c):
    return side_x + side_y + side_z


def triangle_area(side_x=a, side_y=b, side_z=c):
    p = (side_x + side_y + side_z) / 2
    return sqrt(p * (p - side_x) * (p - side_y) * (p - side_z))
