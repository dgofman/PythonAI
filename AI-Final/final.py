
from datetime import datetime
from time import mktime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

epoc = lambda t : int(mktime(datetime.strptime(t, "%Y%m%dT%H%M%S").timetuple()))
data = pd.read_csv('dataexport_20221029T025321.csv', sep=',', converters={'Timestamp': epoc})

print(data.head(5))
print('The shape of our feature is:', data.shape)
data.describe()

data = pd.get_dummies(data)
data.head(5)

labels = np.array(data['Temperature'])
data = data.drop('Temperature', axis=1)
data_list = list(data.columns)
print('Temperature (Y):', labels)
print('Columns (X):', data_list)

data = np.array(data)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.30,random_state=4)

print('Training data shape:', X_train.shape)
print('Training labels shape:', y_train.shape)
print('Testing data shape:', X_test.shape)
print('Testing label shape:', y_test.shape)
rf = RandomForestRegressor(n_estimators=1000, random_state=4)
print('Wait...')
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)
print(predictions)
errors = abs(predictions - y_test)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(rf.score(X_test, y_test)))

# Visualising the Random Forest Regression results
x_ax = range(len(y_test))
plt.plot(x_ax, y_test, linewidth=1, label="original")
plt.plot(x_ax, predictions, linewidth=1.1, label="predicted")
plt.title("y-test and y-predicted data")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()