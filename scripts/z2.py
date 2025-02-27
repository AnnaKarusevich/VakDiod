import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

# x=np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44]) 
# y=np.array([0,1,8,14,28,38,54,74,100]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 


x=np.array([0,0.3,0.6,1,1.3,1.5,1.8,2.2,2.5,2.7,2.9,3.2,3.4,3.6,3.9,4.1,4.4,4.7,5,5.5,5.7,6,6.3,6.5,6.9,7.3,7.5,8.2,8.6,9,9.4,9.7,9.9,10.5,10.9,11.3,11.8,12.4,13.7,15,20,27.4,36,42.7,50.1,55,60,70.7,83,90.9,100,108.3,120]) 
y=np.array([0.76,0.85,0.95,1.05,1.15,1.25,1.35,1.47,1.58,1.68,1.77,1.86,1.95,2.05,2.17,2.26,2.38,2.53,2.67,2.88,2.98,3.13,3.29,3.41,3.6,3.83,3.96,4.3,4.56,4.78,5.01,5.17,5.3,5.62,5.84,6.08,6.42,6.76,7.57,8.33,11.38,13.77,14.04,14.17,14.28,14.35,14.41,14.53,14.63,14.73,14.82,14.89,14.99]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 


# x=np.array([0,19.8,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
# y=np.array([0,0.008,0.015,0.022,0.033,0.059,0.071,0.092,0.13,0.17,0.227,0.301,0.375,0.455,0.62,0.74,0.985]) 
# plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

# plt.legend(('$\phi_з=40В$','$\phi_з=45В$','$\phi_з=50В$'),loc=(0.1,0.4))

ax.plot(x,y,'ko', color = "teal", markersize=4) 
plt.title('ВАХ диода при токе накала 1.5 А')
plt.xlabel('$U_a$,В') 
plt.ylabel('$J_a$,мА') 
plt.grid () 
plt.xlim([-1,130]) 
plt.ylim([0,16.5]) 
plt.savefig('z2.png',dpi=300)
plt.show()