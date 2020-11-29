#Program calculates geometric characteristics of polygons

#Asking how many points will polygon has 
n = int (input("Enter number of points your polygon would has "))

#Asking coordinates of the points
print ("Enter coordinates for every point in counter clockwise order:")

#creating empty lists for coordinates
x = []
y = []

#filling lists
i=0
while i<n:
    xi = float (input(f"Enter x{i+1}: "))
    x.append(xi)
    yi = float (input(f"Enter y{i+1}: "))
    y.append(yi)
    i=i+1
x.append(x[0])
y.append(y[0])
print ()

#priinting table of points and coordinates
print("Point"+" "*10+"x"+" "*10+"y")
print ("-"*30)
for i in range(n):
    print (f"{i+1} {x[i]:16.2f} {y[i]:10.2f}")
print ()

#calculating geometrical characteristics
Ax = 0.0
Sx = 0.0
Sy = 0.0
Ix = 0.0
Iy = 0.0
Ixy = 0.0

i=0
for i in range(n):
    Ax=0.5*(x[i+1]+x[i])*(y[i+1]-y[i])+Ax
    Sx=(-1/6)*(x[i+1]-x[i])*(y[i+1]**2+y[i]*y[i+1]+y[i]**2)+Sx
    Sy=(1/6)*(y[i+1]-y[i])*(x[i+1]**2+x[i]*x[i+1]+x[i]**2)+Sy
    Ix=(-1/12)*(x[i+1]-x[i])*(y[i+1]**3+y[i+1]**2*y[i]+y[i+1]*y[i]**2+y[i]**3)+Ix
    Iy=(1/12)*(y[i+1]-y[i])*(x[i+1]**3+x[i+1]**2*x[i]+x[i+1]*x[i]**2+x[i]**3)+Iy
    Ixy=(-1/24)*(y[i+1]-y[i])*((y[i+1]*(3*x[i+1]**2+2*x[i+1]*x[i]+x[i]**2)+y[i]*(3*x[i]**2+2*x[i+1]*x[i]+x[i+1]**2)))+Ixy

Xt = Sy/Ax
Yt = Sx/Ax
Itx = Ix-(Yt**2)*Ax
Ity = Iy-(Xt**2)*Ax
Itxy =Ixy+Xt*Yt*Ax

print ("Geometric characteristics:")
print (f"Ax={Ax:3.2f}")
print (f"Sx={Sx:3.2f}")
print (f"Sy={Sy:3.2f}")
print (f"Ix={Ix:3.2f}")
print (f"Iy={Iy:3.2f}")
print (f"Ixy={Ixy:3.2f}")
print (f"Xt={Xt:3.2f}")
print (f"Yt={Yt:3.2f}")
print (f"Itx={Itx:3.2f}")
print (f"Ity={Ity:3.2f}")
print (f"Itxy={Itxy:3.2f}")