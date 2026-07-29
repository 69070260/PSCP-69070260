"""ผสมสี"""

Cl1 = input()
Cl2 = input()

if Cl1 == "Red":
    if Cl2 == "Red":
        print("Red")
    elif Cl2 == "Yellow":
        print("Orange")
    elif Cl2 =="Blue":
        print("Violet")
    else:
        print("Error")

elif Cl1 == "Yellow":
    if Cl2 == "Yellow":
        print("Yellow")
    elif Cl2 == "Red":
        print("Orange")
    elif Cl2 == "Blue":
        print("Green")
    else:
        print("Error")

elif Cl1 == "Blue":
    if Cl2 == "Blue":
        print("Blue")
    elif Cl2 == "Red":
        print("Violet")
    elif Cl2 == "Yellow":
        print("Green")
    else:
        print("Error")

else:
    print("Error")
