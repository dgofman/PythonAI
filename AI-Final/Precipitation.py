import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

from sys import modules
from time import mktime
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#https://www.meteoblue.com/en/weather/archive/export/basel_switzerland_2661604?daterange=2022-01-01%20-%202022-10-29&domain=NEMSAUTO&min=2022-10-22&max=2022-10-29&params%5B%5D=&params%5B%5D=temp2m&params%5B%5D=&params%5B%5D=&params%5B%5D=precip&params%5B%5D=&params%5B%5D=&params%5B%5D=&params%5B%5D=&params%5B%5D=wind%2Bdir10m&utc_offset=0&timeResolution=hourly&temperatureunit=FAHRENHEIT&velocityunit=MILE_PER_HOUR&energyunit=watts&lengthunit=metric&degree_day_type=10%3B30&gddBase=10&gddLimit=30
epoc = lambda t : int(mktime(datetime.strptime(t, '%Y%m%dT%H%M%S').timetuple()))
data = pd.read_csv('dataexport_20221029T025321.csv', sep=',', converters={'Timestamp': epoc})

print(data.head(5))
print('The shape of our feature is:', data.shape)
data.describe()

data = pd.get_dummies(data)
data.head(5)

labels = np.array(data['Precipitation'])
data = data.drop('Precipitation', axis=1)
data_list = list(data.columns)
print('Precipitation (Y):', labels)
print('Columns (X):', data_list)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.10,random_state=2)

print('Training data shape:', X_train.shape)
print('Training labels shape:', y_train.shape)
print('Testing data shape:', X_test.shape)
print('Testing label shape:', y_test.shape)
rf = RandomForestRegressor(n_estimators=2000, random_state=2)
print('Wait...')
rf.fit(X_train, y_train)
predictions = rf.predict(X_test)
errors = abs(predictions - y_test)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(rf.score(X_test, y_test)))

# Visualising the Random Forest Regression results

# sort values begin
order_list= []
keys = X_test['Timestamp'].keys()
for i, k in enumerate(keys):
    order_list.append({'index': i, 'value': k})
order_list = sorted(order_list, key=lambda item: item['value'])

x_values = []
y1_values = []
y2_values = []
for item in order_list:
    index = item['index']
    x_values.append(X_test['Timestamp'].values[index])
    y1_values.append(y_test[index]) #test data 
    y2_values.append(predictions[index]) #predicted data
# sort values end

def format(x, _):
    index = int(x)
    if index < len(x_values):
        ts = x_values[index]
    else:
        ts = x_values[-1]
    return datetime.fromtimestamp(ts).strftime('%m/%d/%Y, %H:%M')

length = len(x_values)
x_ax = range(length)
plt.figure(figsize=(25, 10))
plt.xlim(0, length)
plt.plot(x_ax, y1_values, linewidth=1, label='Original')
plt.plot(x_ax, y2_values, linewidth=1.1, label='Predicted')
plt.title('Precipitation predicted data')
plt.xlabel('Timestamp')
plt.ylabel('Precipitation')
plt.legend(loc='best',fancybox=True, shadow=True)

ax = plt.gca()
ticks_loc = ax.get_xticks()
ax.xaxis.set_major_locator(ticker.FixedLocator(ticks_loc))
ax.set_xticklabels(ticks_loc, rotation=45, ha='right', rotation_mode='anchor')
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.1f}mm'.format(y)))

plt.grid(True)
plt.tight_layout()

# Skip following lines in the Google Colab and Jupyter Notebook (not interactive)
if not 'mplcursors' in modules.keys():
    from mplcursors import cursor 
    tooltip = cursor(hover=True)
    tooltip.connect(
        'add', lambda sel: sel.annotation.set(
                    text=sel.artist.get_label() + '\n' + 
                    '{}'.format(ax.format_coord(*sel.target)
                        .replace('x=', 'Timestamp: ')
                        .replace('y=', '\nPrecipitation: '))   
        ))
    plt.show()