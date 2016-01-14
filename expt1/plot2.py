from numpy import *
from matplotlib.pyplot import *



x2=[0.0,2.29,2.74,3.06,3.48,3.91,4.5,4.99,5.61,6.9,7.45,8.19,9.08,9.78,10.2];
y2=[0.0,.139,.324,.556,.0926,1.389,2.176,2.870,3.889,6.343,7.454,9.028,11.11,12.685,14.167];
for i in range(0,len(y2)):
    y2[i]=y2[i]/558
coefficients = polyfit(x2, y2, 2)
polynomial = poly1d(coefficients)
xs2 = arange(0, 10.2, 0.1)
ys2 = polynomial(xs2)
print xs2
print ys2


title('Id versus Vgs curve for Vds neraly equal to 6V')
plot(x2, y2,'o')
plot(xs2, ys2,'g')
ylabel('Id(mA)')
xlabel('Vgs(V)')
show()

