import matplotlib.pyplot as plt

y1 = [6103.072,	11124.06,	15893.85,	21793.92,	29101.02]
y2 = [4607.012,	9871.915,	14017.06,	21058.24,	27177.26]


x1 = [2000, 4000, 6000, 8000, 10000]
x2 = x1


plt.plot(x1, y1, label= "BST_Insertion" , marker = 'o' ,markersize = 5 , color = 'blue', markerfacecolor = 'black')
plt.plot(x2, y2, label="BST_Deletion" , marker = 'o' ,markersize = 5 , color = 'yellow' , markerfacecolor = 'black')


plt.ylabel('Time (micro-second)')
plt.xlabel('Number of Element in Array')
plt.title('For Array A[]')
plt.legend()
plt.show()
