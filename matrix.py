
fl=open("image6.ppm","w")
initialstr="P3\n500 500\n255\n"
data=list(range(250000))
initVal=0
while(initVal<len(data)):
    data[initVal]=["0","0","0"]
    initVal+=1
def plot(x,y,color):# color is a list
    x+=250
    y=250-y
    data[x+y*500]=color

#for the first two octants, the x0 must be smaller than x1
def firstoct(x0,y0,x1,y1,color):#oct 1 and 5
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=2*A+B
    while x<x1:
        plot(x,y,color)
        if d>=0:
            y+=1
            d=d+2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def secondoct(x0,y0,x1,y1,color):#oct 2 and 6
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d<=0:
            d=d+2*A
            x+=1
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def thirdoct(x0,y0,x1,y1,color):#oct 3 and 7 remember the x0 and x1 hierarchy is reversed for this one
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<y1:
        plot(x,y,color)
        if d>=0:
            x=x-1
            d=d-2*A
        y=y+1
        d=d+2*B
    plot(x1,y1,color)
def fourthoct(x0,y0,x1,y1,color): #oct 4 and 8
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while x<x1:
        plot(x,y,color)
        if d<=0:
            y=y-1
            d=d-2*B
        x=x+1
        d=d+2*A
    plot(x1,y1,color)
def oneSlopePos(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y+=1

def oneSlopeNeg(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while x<=x1:
        plot(x,y,color)
        x+=1
        y-=1
def zeroSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while(x<=x1):
        plot(x,y,color)
        x+=1
def undefinedSlope(x0,y0,x1,y1,color):
    x=x0
    y=y0
    while y<=y1:
        plot(x,y,color)
        y+=1

def drawline(x0,y0,x1,y1,color):# whenever possible x0 must be greater than x1(left to right orientation)
    if(x0==x1):
        undefinedSlope(x0,y0,x1,y1,color)
    elif(y0==y1):
        zeroSlope(x0,y0,x1,y1,color)
    elif abs(x1-x0)>=abs(y1-y0):
        if y1>y0:
            firstoct(x0,y0,x1,y1,color)
        else:
            fourthoct(x0,y0,x1,y1,color)
    else:
        if y1>y0:
            secondoct(x0,y0,x1,y1,color)
        else:
            thirdoct(x1,y1,x0,y0,color)



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
def update_matrix(row,column,matrix,value):
    matrix[column][row]=value
def print_matrix(matrix):
    result=""
    row=len(matrix[0])
    col=len(matrix)
    for x in range(row):
        for y in range(col):
            add=str(matrix[y][x])
            if len(add)==1:
                result+=add+"   "
            elif len(add)==2:
                result+=add+"  "
            else:
                result+=add+" "
        result+="\n"
    print(result)
        


def ident(matrix):
    row=len(matrix[0])
    col=row
    for x in range(row):
        for y in range(col):
            if(x==y):
                matrix[y][x]=1
            else:
                matrix[y][x]=0
def matrix_multiplication(m1,m2):
    result=new_matrix(len(m1[0]),len(m2))
    for secondCol in range(len(m2)):
        for y in range(len(m1[0])):
            add=0
            for x in range(len(m1)):
                add+=(m1[x][y]*m2[secondCol][x])
            result[secondCol][y]=add
    for x in range(len(m2)):
        m2[x]=result[x]
    
def empty_matrix():
    m = []
    m.append( [] )
    return m
#test cases
m1=new_matrix(2,2)
m2=new_matrix(2,3)
update_matrix(0,0,m1,1)
update_matrix(0,1,m1,2)
update_matrix(1,0,m1,3)
update_matrix(1,1,m1,4)
update_matrix(0,0,m2,5)
update_matrix(0,1,m2,6)
update_matrix(0,2,m2,7)
update_matrix(1,0,m2,8)
update_matrix(1,1,m2,9)
update_matrix(1,2,m2,0)
#that ends here
def add_point(matrix,x,y,z=0):
    if len(matrix[0])==0:
        matrix[0].append(x)
        matrix[0].append(y)
        matrix[0].append(z)
        matrix[0].append(1)
    else:
        matrix.append([])
        matrix[len(matrix)-1].append(x)
        matrix[len(matrix)-1].append(y)
        matrix[len(matrix)-1].append(z)
        matrix[len(matrix)-1].append(1)
def add_edge(matrix,x0,y0,z0,x1,y1,z1):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
def add_lines(matrix,color):
    step=0
    while(step<len(matrix)):
        #print("x0:"+str(matrix[step][0])+"  "+"y0:"+str(matrix[step][1])+"  "+"x1:"+str(matrix[step+1][0])+"  "+"y1:"+str(matrix[step+1][1]))
        drawline(matrix[step][0],matrix[step][1],matrix[step+1][0],matrix[step+1][1],color)
        step+=2
#example
diagram=empty_matrix()
add_edge(diagram,0,0,0,50,50,0)
add_edge(diagram,50,0,0,100,50,0)
add_edge(diagram,100,0,0,100,50,0)#
add_edge(diagram,50,-50,0,100,0,0)#
add_edge(diagram,0,-50,0,50,-50,0)#
add_edge(diagram,0,-50,0,0,0,0)
add_edge(diagram,50,50,0,100,50,0)
add_edge(diagram,0,0,0,50,0,0)
add_edge(diagram,50,-50,0,100,0,0)
add_edge(diagram,50,-50,0,50,0,0)#this one
add_lines(diagram,["255","255","255"])
for ls in data:
    for a in ls:
       initialstr+=a+" "
    initialstr+=" "
fl.write(initialstr)
matrix1=empty_matrix()
matrix2=empty_matrix()
add_edge(matrix1,0,1,0,4,5,0)
add_edge(matrix1,4,5,0,1,2,0)
add_edge(matrix2,0,3,0,6,8,0)
print("Name of image file: image6.ppm")
print("testing add edge (matrix2,0,3,0,6,8,0)")
print_matrix(matrix2)
print("testing matrix multiplication m1*m2")
print_matrix(matrix1)
print_matrix(matrix2)
print("after matrix multiplication m2 is :")
matrix_multiplication(matrix1,matrix2)
print_matrix(matrix2)


fl.close()

