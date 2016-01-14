from numpy import *
from matplotlib.pyplot import *



x2=[.81,.95,1.1,1.49,2.28,3.0,3.79,4.76,5.50,6.26,8.37,9.68,4.73];
y2=[1.60,1.74,1.86,1.97,2.02,2.04,2.05,2.07,2.08,2.09,2.11,2.13,2.06];
for i in range(0,len(y2)):
    y2[i]=y2[i]/558
coefficients = polyfit(x2, y2, 6)
polynomial = poly1d(coefficients)
xs2 = arange(0, 8.37, 0.1)
ys2 = polynomial(xs2)
print xs2
print ys2
# plt.plot(vds,vm,'o')
# plt.xlabel('Vds for V')
# plt.ylabel('vm')
# plt.show()

x3=[0.39,0.40,.45,.48,.52,.60,.68,.81,1.05,1.10,1.27,1.58,2.01,4.06,5.21,2.89,2.36];
y3=[1.66,1.69,1.89,2.02,2.14,2.44,2.73,3.14,3.88,3.96,4.41,5.07,5.70,6.3,6.32,6.16,5.97];
for i in range(0,len(y3)):
    y3[i]=y3[i]/558
coefficients3 = polyfit(x3, y3, 6)
polynomial3 = poly1d(coefficients3)
xs3 = arange(0, 5.21, 0.1)
ys3 = polynomial3(xs3)
print xs3
print ys3

x1=[.45,.49,.54,.61,.65,.76,.97,.98,1.07,1.15,1.22,1.35,1.51,1.88,2.54];
y1=[1.63,1.84,2.04,2.15,2.32,2.63,2.93,3.22,3.39,3.56,3.71,3.97,4.2,4.61,4.89];
for i in range(0,len(y1)):
    y1[i]=y1[i]/558
coefficients1 = polyfit(x1, y1, 6)
polynomial1 = poly1d(coefficients1)
xs1 = arange(0, 5.21, 0.1)
ys1 = polynomial3(xs3)
print xs1
print ys1

title('Vds vs Id curve for different values of Vgs')
plot(x1,y1,'o')
plot(x2, y2,'o')
plot(x3,y3,'o')
plot(xs1,ys1,'b')
plot(xs2, ys2,'g')
plot(xs3,ys3,'r')
ylabel('Id')
xlabel('Vds')
show()



