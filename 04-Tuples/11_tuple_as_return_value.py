#tuple as return value

def get_coordinates():
    x=int(input("enter x: "))
    y=int(input("enter y: "))
    return (x, y)
coordinates=get_coordinates()
print("Coordinates:",coordinates)
