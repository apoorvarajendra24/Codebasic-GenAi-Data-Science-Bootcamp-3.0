def cylinder_volume(radius,height):     # you can fix value for parameters if you dont want to pass it as(height = 6)
    print("radius: ",radius)
    print("height: ",height)
    volume = 3.14 * (radius**2) * height
    return volume

def triangle_area(base, height):
    print("base: ",base)
    print("height:",height)
    area = (base*height)/2
    return area