

def get_shape():
    shapes = ["pyramid","square","triangle","rectangle","parallelogram","diamond",'inverse_pyramid']
    while True:
        shape = input("Shape?: ")
        shape = shape.lower()
        if shape in shapes:
            return shape

 

def get_height():
    try:
        height=int(input('Height?: Height?:'))
    except ValueError:
        return 1

    if height>80:
        return get_height()
    else:
        return (height)


def draw_pyramid(height, outline):
    if outline:
        for i in range(1, height +1):
            for j in range(1,height * 2):
                if j - i == height - 1 or j + i == height + 1 or i == height:
                    print("*",end="")
                elif j - i < height - 1:
                    print(end=" ")
            print()
    else:
        k = 0
        for i in range(1, height +1):
            for j in range(1, (height-i)+1):
                print(end=" ")
            while k!=(2*i-1):
                print("*",end="")
                k +=1
            k = 0
            print()
            
        

def draw_square(height,outline):
    if outline==True:
        for i in range(height):
            for j in range(height):
                if(i ==0 or i == height-1 or j == 0 or j ==height-1):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

    else:
        for i in range(height):
            for j in range(height):
                print('*' ,end="" )
            print()
    

 
def draw_triangle(height, outline):
    if outline==True:
        for i in range(1,height+1):
            for j in range(1,i+1):
                if i == 1 or i == height or j == 1 or j ==i:
                    print("*",end="")
                else:
                    print(end=" ")
            print()
    else:
        for i in range(height):
            for j in range(i+1):
                print("*", end="")
            print()

def draw_rectangle(height ,outline):
    if outline==True:
        column = height+2
        for i in range(height):
            for j in range(column):
                if i == 0 or i == height-1 or j ==0 or j == column-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    else:
        for i in range(1,height+1):
            for j in range(1,height*2+1): #*2 so that it prints a rectangle instead of a square
                print("*",end=" ")
            print()

def draw_parallelogram(height ,outline):
    if outline==True:
        for k in range(height):
            for t in range(height-k-1): #the -k makes it print the parallelogram instead of a rectangle
                print(" ",end="")
            for a in range(height):
                if (a==0) or (k==0) or (a==height-1 ) or (k==height-1):
                    print("*", end="")
                else:
                    print(" ",end="")
            print() #moves the control to a new line
            
    else:
        for i in range( height):
            print(" "*(height-i)+" *"*(height+1))

def draw_inverse_pyramid(height ,outline):
    if outline ==True:
         for i in range(height-1,0 ,-1):
            for j in range(1,height-i+1):
                print(" ",end="")
            for j in range(1, 2*i):
                if j==1 or j==2*i-1 or i==height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    else:
        for i in range(height,0,-1):
            for j in range(height - i):
                print(end=" ")
            for col in range(i*2-1):
                print("*", end="")
            print()
        
        
        
def draw(shape, height, outline):
    if shape_param == "pyramid":
         return draw_pyramid(height,outline)
    elif shape_param == "square":
        draw_square(height,outline)
    elif  shape_param == "triangle":
        draw_triangle(height, outline)
    elif shape_param == "rectangle":
        draw_rectangle(height, outline)
    elif shape_param == "parallelogram":
        draw_parallelogram(height ,outline)
    elif shape_param == "inverse_pyramid":
        draw_inverse_pyramid(height, outline)

    

def get_outline():
    outline = str(input("Outline? "))
    if outline == "y".lower() or outline == "":
        return True
    elif outline == "n".lower():
        return False
    else:
        return get_outline

if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

