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
    d = float(vI)*float(t)+(1/2)*float(a)*float(t)^2
    print(str(d))
    return d

def solveT():
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    a = input("Enter acceleration (in m^2/2): ")
    if vF == null:
        d = input("Enter distance (in Meters): ")
        t = (-float(vI) + sqrt(float(vI)^2 + 2*float(a)*float(d)))/float(a)
    else:
        t = (float(vF) - float(vI))/float(a)
    print(str(t))
    return t

def solveA():
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = input("Enter Final Velocity (in m/s): ")
    d = input("Enter distance (in Meters): ")
    a = ((float(vF)**2 - float(vI)**2)/2)/int(d)
    print(str(a))
    return a

def solveVI():
    a = input("Enter acceleration (in m^2/2): ")
    d = input("Enter distance (in Meters): ")
    vF = input("Enter Initial Velocity (in m/s): ")
    vI = 2*float(a)*float(d)+sqrt(float(vF))
    vIConfirmed = (float(vI)^2 - float(vF)^2)-(2*float(a)*float(d))
    if vIConfirmed == 0:
           print(str(vI))
    else:
        print("Error in equation")
    return vI

def solveVF():
    a = input("Enter acceleration (in m^2/2): ")
    t = input("Enter time (in seconds): ")
    vI = input("Enter Initial Velocity (in m/s): ")
    vF = float(vI) + float(a)*float(t)
    print(str(vF))
    return vF

#prompt for accelerated motion questions, to determine which equation to use
def acceleratedMotion():
    print("1 - Acceleration")
    print("2 - Time")
    print("3 - Initial Velocity")
    print("4 - Final Velocity")
    print("5 - Distance")
    k = input("Enter the number corresponding to the variable you need to solve for: ")
    def chooseEquation(k):
        switcher={
            1:'a - Acceleration',
            2:'t - Time',
            3:'vI - Initial Velocity',
            4:'vF - Final Velocity',
            5:'d - Distance'
            }
        return switcher.get(k, "Invalid Input")
    print("Solving for: ")
    chooseEquation(k)
    switcher={
        1:solveA(),
        2:solveT(),
        3:solveVI(),
        4:solveVF(),
        5:solveD()
        }
    return switcher.get(k)


def main():
    choice = input("Please enter 1 for gravity and 2 for accelerated motion: ")
    if choice == 1:
        gravity()
    else:
        acceleratedMotion()

main()
