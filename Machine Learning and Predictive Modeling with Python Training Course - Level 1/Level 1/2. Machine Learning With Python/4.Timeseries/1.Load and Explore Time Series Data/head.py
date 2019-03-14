'''
@author: "Mohamed Jelidi"
@email : "jelidi.mohamad@gmail.com"
'''

# summarize first few lines of a file
from pandas import Series
series = Series.from_csv('daily-total-female-births.csv', header=0)
print(series.head(10))