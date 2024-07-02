import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
inputvalues = [1,2,3,4,5]
plt.style.use('seaborn-darkgrid')
fig,ax = plt.subplots()
ax.plot(inputvalues,squares,linewidth = 3)
ax.set_title("sqares",fontsize=24)
ax.set_xlabel("x",fontsize = 14)
ax.set_ylabel("Y",fontsize=14)
ax.tick_params(axis ='both',labelsize = 14)
print(plt.style.available)
plt.show()

