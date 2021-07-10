from matplotlib.pyplot import *
from math import *
np=500
xi=1
xf=5
h=(xf-xi)/(np-1)
k=3.0
x=[0.0]*np
y=[0.0]*np
s=[0.0]*np
y1=[0.0]*np
for i in range (0,np):
	x[i]=xi+i*h
	s[i]=log(x[i])
	y[i]=log(k)+s[i]
	y1[i]=k*x[i]
	
	
	
plot(s,y,'.-r',x,y1,'.-b',s,y1,'.-g')
xlabel('voltage')
ylabel('current')
legend(['log y vs log x', 'y vs x','y vs logx'])
title('analog HW (AR SIR)')
savefig('practice3.png')
show()
