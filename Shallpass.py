import math
#Take robot measurments

height = int(input("Enter robot height:"))
width = int(input("Enter robot width: "))

#Measurments Set

#Start of the endless Loop

x = 0

while x != 1:
    # Adjusting gateway object type
    type = int(input("What is the type of the object(1(Type Circle)-2(Type Rectangle)-3(Type Triangle))"))
    
    if type == 1:
        
        #Type Circle
        #Setting the max values by looking at radius and the diameter
        #If the robots height is smaller than the radius and its width is smaller than the diameter it will pass.

        diameter = int(input("What is the diameter of the circle?"))
                           

        #Calculate area by common formula

        print(((diameter/2)**2)*math.pi)

        #Compare results

        if diameter > width and diameter/2 > height: 
            print("True")
        else:
            print("False")
    
    
    elif type == 2:
        
        #Type Rectangle
        #Setting the max values with looking at the gateways measurements
        #The robots width and height values must be smaller than the max values if the robot want to pass

        max_width = int(input("What is the width of the gateway?"))
        max_height = int(input(" What is the height of the gateway?"))

        #Calculate area by using common formula
        max_area = max_width*max_height
        print(max_area)

        #Compare results with the robot
        if max_width > width and max_height > height:
            print("True")
        else:
            print("False")

    elif type == 3:
        
        #Type Triangle
        #Get equalliteral trinagles one side
        side = int(input("Enter the side of equalliteral:"))
        
        #First find the max enterable width by dividing the equaliteral triangles one side by two
        #This value must be bigger than the robots width if the robot wants to pass.
        max_width = side/2
        
        #Next we are going to find the max enterable height by using the pisagor thorem.
        #By means we are going to solve a equation of(x is the one side of the equaliteral.)
        # x*x/4 = x*x/16 + y ==> y = x root 3 over 4
        #This result will give the max height that could pass

        max_height = (side* math.sqrt(3))/4
        
        #Calculate area of the gateway by using the common formula
        print(((side**2)*math.sqrt(3))/4)

        #Compare the results with the robot

        if max_height > height and max_width > width:
            print("True")
        else:
            print("False")





    else:
        #Error Message
        print("Please select an exsisting object")
    
    
