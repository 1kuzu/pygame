import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues ,s = 10)
ax.set_title('squares',fontsize = 24)
ax.set_xlabel('X',fontsize = 14)
ax.set_ylabel('Y',fontsize = 14)
ax.tick_params(axis = 'both',which = 'major',labelsize = 14)
ax.axis([0,1100,0,1100000])
plt.show()
# plt.savefig('scatter.png',bbox_inches='tight')