import matplotlib.pyplot as plt
labels=['English', 'Math', 'Science', 'History']
size=[45,30,15,10]

plt.clf()
plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen','lightcoral','lightsalmon'])

plt.title("Subjects Distribution")
plt.show()