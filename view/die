from random import randint 
import matplotlib.pyplot as plt
class Die:
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die_1=Die()
a = die_1.roll()

results = []
for _ in range(1,101):
    result = die_1.roll()
    results.append(result)

print(results)
print(len(results))

x = range(1,101)
y = results

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x,y,c='red',s = 10)
ax.set_title('squares',fontsize = 24)
ax.set_xlabel('hit',fontsize = 14)
ax.set_ylabel('number',fontsize = 14)
ax.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.show()


