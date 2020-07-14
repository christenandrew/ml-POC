import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NBL&apikey=ZCB343AS7CKA7S67
csv_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NBL&outputsize=full&datatype=csv&apikey=ZCB343AS7CKA7S67'
df = pd.read_csv(csv_url)
df['timestamp'] = pd.to_datetime(df.timestamp)
print(df)
df.sort_values(by='timestamp', ascending=True)
#sns.scatterplot(x='close', y='volume', data=df)
#sns.pairplot(df)
#sns.distplot(df['volume'])
#df[['timestamp','close']].set_index('timestamp').plot()
plt.show()


