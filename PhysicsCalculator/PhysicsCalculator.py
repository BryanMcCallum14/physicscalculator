#Gravitational force between two objects
def gravity():
    G = (6.674*(10^-11))
    m1 = input("Mass of first object (in kg): ")
    m2 = input("Mass of second object (in kg): ")
    r = input("Distance between first and second object (in Meters): ")
    f = (G*(float(m1) * float(m2)))/(int(r)^2)
    print(str(f) + "N/kg")

def acceleratedMotion():
    k = input("Enter the number corresponding to the variable you need to solve for: ")
    switch={
        1:'a - Acceleration',
        2:'t - Time',
        3:'vI - Initial Velocity',
        4:'vF - Final Velocity',
        5:'d - Distance'
        }
    return switch.get(k, "Invalid Input")
    d = input("Enter distance (in Meters): ")
    vI
    vF
    a
    t
