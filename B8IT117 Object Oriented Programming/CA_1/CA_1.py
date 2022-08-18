#CA 1
#Student Name: Jose Maria Rico Leal - 10539218
#Module Name: B8IT117 Object Oriented Programming
#Presentation Date: Tuesday 26th of October

#There is a requirement to import pyplot from matplotlib in order to display any chart
from matplotlib import pyplot as plt

#Open the file, there is no path because it is saved in the same folder as the solution.
file=open('weekly_expenses.txt','r')
#reading all lines
data=file.readlines()

#Close the file
file.close()

#Split the data when we find a ","
data=[i.split(',') for i in data]

#Getting data and starting the range from "0"
data=data[0]

#Convert the numbers from 'weekly_expenses.txt' into integers
data=[int(i) for i in data]

#Assigning labels
labels=["Rent","Gas","Food","Clothing","Car Payment","Misc"]

#Creat objects
fig1, ax1 = plt.subplots()

#Draw the pie
ax1.pie(data, labels=labels, autopct='%1.1f%%')
ax1.axis('equal') # Equal will make a sure that the pie is perfectly round.

#show the plotting
plt.show()