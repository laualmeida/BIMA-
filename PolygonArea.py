#BIM A+ 3 - Parametric Modelling in BIM
#Programming assignment 03

#Laura Almeida

# Ask the user how many points are there for the polygon
print()
n = int(input("Enter the number of polygon points: "))
print()
print("Number of points =",n)
print()

# Create the coordinates list
x = []
y = []

# Ask the user to input the coordinates, starting x and y for the first point, then for the second, so forth
print("Enter x and y coordinates for polygon points ...")
for i in range(0, n):
    input_x = float(input("enter x: "))
    x.append(input_x)
    input_y = float(input("enter y: "))
    y.append(input_y)

# Print the list of coordinates
print()
print(f"{'x':>14}  {'Y':>9}")
print("-"   * 30)

for i in range(0,n):
    print("Point" , i+1 , ":" , f"{x[i]:>5} {y[i]:>10}")

print("-"   * 30)

# Create an empty list for storing the Ax results
list_ax = []
list_sx = []
list_sy = []
list_ix = []
list_iy = []
list_ixy = []

# Insert the results on the Ax list
for i in range (0,n):
    ax = (x[i]+x[i-1]) * (y[i]-y[i-1])
    list_ax.append(ax)

    sx = (x[i]-x[i-1])*(y[i]**2+(y[i-1]*y[i])+y[i-1]**2)
    list_sx.append(sx)

    sy = ((y[i]-y[i-1])*((x[i]**2)+(x[i-1]*x[i])+(x[i-1]**2)))
    list_sy.append(sy)

    ix = (x[i]-x[i-1])*(y[i]**3+(y[i]**2)*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    list_ix.append(ix)
    
    iy = (y[i]-y[i-1])*(x[i]**3+(x[i]**2)*x[i-1]+x[i]*x[i-1]**2+x[i-1]**3)
    list_iy.append(iy)
        
    ixy = (y[i]-y[i-1])*(((y[i])*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2))+y[i-1]*(3*x[i-1]**2+2*x[i]*x[i-1]+x[i]**2))
    list_ixy.append(ixy)
        
# Calculations formula
total_ax=(1/2)*sum(list_ax)
total_sx=(-1/6)*sum(list_sx)
total_sy=(1/6)*sum(list_sy)
total_ix=(-1/12)*sum(list_ix)
total_iy=(1/12)*sum(list_iy)
total_ixy=(-1/24)*sum(list_ixy)

xt=total_sy/total_ax
yt=total_sx/total_ax

Ixt=total_ix-yt**2*total_ax
Iyt=total_iy-xt**2*total_ax
Ixyt=total_ixy+xt*yt*total_ax

# Print output
print()
print("Geometric Characteristics")
print()
print("Ax:    {:.2f}".format(total_ax))
print("Sx:    {:.2f}".format(total_sx))
print("Sy:    {:.2f}".format(total_sy))
print("Ix:    {:.2f}".format(total_ix))
print("Iy:    {:.2f}".format(total_iy))
print("Ixy:  {:.2f}".format(total_ixy))
print("xt:    {:.2f}".format(xt))
print("yt:    {:.2f}".format(yt))
print("Ixt:   {:.2f}".format(Ixt))
print("Iyt:   {:.2f}".format(Iyt))
print("Ixyt:  {:.2f}".format(Ixyt))
print()
print("Thank you! :)")
print("Laura Almeida")