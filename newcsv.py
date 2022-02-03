import pandas
import numpy
import matplotlib.pyplot as pyplot

#importing our csv
dataset  = pandas.read_csv("forecasting_truncated-1.csv")
print(dataset.describe())

#the next lines create a new dataframe to visualize the data
newframe = pandas.DataFrame()
#add stuff to the newframe 
for stuff in range(len(dataset)):
	val = stuff + 1
	newframe = newframe.append({'Months': val}, ignore_index = True)
	print(newframe.loc[stuff])

newframe['Sales'] = pandas.Series(dataset['sales'])
#plotting the data to look for trends
newframe.plot(kind = 'scatter',
       x = 'Months',
       y = 'Sales',
       color = 'red')
  
# set the title
pyplot.title('ScatterPlot')
# show the plot
pyplot.show()
#clearly month 1 is always high while 11/12 are low
#the trend looks to be pretty linear linear overall

#now I will add dummy variables for those months
newframe['M12'] = 0
newframe['First2'] = 0
#changing the appropriate dummy variables
m = 11
while m < 146:
	newframe['M12'][m]= 1
	m += 12
m = 0
while m < 140:
	newframe['First2'][m]= 1
	m += 12
m = 1
while m < 140:
	newframe['First2'][m]= 1
	m += 12
#checking everything 
print(newframe.to_string())
#saving the new dataframe as a csv
newframe.to_csv("CSV/forecastchallenge.csv", index= False)
