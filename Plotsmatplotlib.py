import numpy as np 
from matplotlib import pyplot as plt 
x = np.linspace(0,10,1000)
plt.plot(x,np.sin(x))
plt.show()

plt.plot(x,np.sin(x), color= 'green', linestyle= 'dashdot', label= 'sin(x)')
plt.plot(x,np.cos(x), color= 'blue', linestyle= 'dashdot', label= 'cos(x)')
plt.legend()
plt.show()

x = np.linspace(0,10,1000)
fig, ax = plt.subplots(2,2)
ax[0,0].plot(x, np.sin(x), label='sin(x)')
ax[0,0].legend()
ax[0,1].plot(x, np.cos(x))
ax[1,0].plot(x, np.tan(x))

x = np.linspace(0,10,1000)
fig, ax = plt.subplots(3)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.tan(x))


CS= [45, 33, 10, 20, 38]
IT= [40, 10, 20, 13, 34]

barwidth = 0.25
bar1 = np.arange(len(CS))
bar2= [x+barwidth for x in bar1]

plt.bar(bar1, CS, width= barwidth, label= 'CS')
plt.bar(bar2, IT, width= barwidth, label= 'IT')
plt.xticks(bar1, ['2017', '2018', '2019', '2020', '2021'])
plt.xlabel('Year')
plt.ylabel('No of students')
plt.show()


x = np.random.rand(10)
y = np.random.rand(10)

x2 = np.random.rand(10)
y2 = np.random.rand(10)

plt.scatter(x,y, marker= '*')
plt.scatter(x2,y2, marker= 's')

data= [20, 10, 45, 87, 23, 72, 27, 90, 67]

plt.hist(data, bins=[0, 20,40,60,80,100], width= 10)

branch= ['CS', 'IT', 'EC', 'ME', 'CE']
values= [30, 10, 25, 12, 18]
plt.pie(values, labels=branch)
plt.show()