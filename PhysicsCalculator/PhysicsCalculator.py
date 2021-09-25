#Gravitational force between two objects
def gravity():
    G = (6.674*(10^-11))
    m1 = input("Mass of first object (in kg): ")
    m2 = input("Mass of second object (in kg): ")
    r = input("Distance between first and second object (in Meters): ")
    f = (G*(float(m1) * float(m2)))/(int(r)^2)
    print(str(f) + "N/kg")
    return f

#seperated equations for solving accelerated motion problems
def solveD():
    vI = input("Enter Initial Velocity (in m/s): ")
    t = input("Enter time (in seconds): ")
    a = input("Enter acceleration (in m^2/2): ")
    d = vI*t+(1/2)*a*t^2
    return d

def solveT():
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    a = input("Enter acceleration (in m^2/2): ")
    if vF == null:
        d = input("Enter distance (in Meters): ")
        t = (-vI + sqrt(vI^2 + 2*a*d))/a
    else:
        t = (vF - vI)/a
    return t

def solveA():
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    d = input("Enter distance (in Meters): ")
    a = ((vF^2 - vI^2)/2)/d
    return a

def solveVI():
    a = input("Enter acceleration (in m^2/2): ")
    d = input("Enter distance (in Meters): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    vI = 2*a*d+sqrt(vF)
    vIConfirmed = (vI^2 - vF^2)-(2*a*d)
    if vIConfirmed == 0:
           print(str(vI))
    else:
        print("Error in equation")
    return vI

def solveVF():
    a = input("Enter acceleration (in m^2/2): ")
    t = input("Enter time (in seconds): ")
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = vI + a*t
    return vF

#prompt for accelerated motion questions, to determine which equation to use
def acceleratedMotion():
    k = input("Enter the number corresponding to the variable you need to solve for: ")
    print("1 - Acceleration")
    print("2 - Time")
    print("3 - Initial Velocity")
    print("4 - Final Velocity")
    print("5 - Distance")
    def chooseEquation(k):
        switch={
            1:'a - Acceleration',
            2:'t - Time',
            3:'vI - Initial Velocity',
            4:'vF - Final Velocity',
            5:'d - Distance'
            }
        return switch.get(k, "Invalid Input")
    print("Solving for: ")
    chooseEquation(k)
    switch={
        1:0,
        2:1,
        3:2,
        4:3,
        5:4
        }
    d = input("Enter distance (in Meters): ")
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    a = input("Enter acceleration (in m^2/2): ")
    t = input("Enter time (in seconds): ")

    d = vI*t + (1/2)*a*t^2
    vF = vI + a*t
    vI = 0
    a = 0
    t = 0
