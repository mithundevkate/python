#import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='pearl')

df = pd.read_csv('http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt', sep='\t')
df2007 = df[df.year==1996]
df.head(2)

df2007.iplot(kind='bubble', x='gdpPercap', y='lifeExp', size='pop', text='country',
             xTitle='GDP per Capita', yTitle='Life Expectancy',
             filename='cufflinks/simple-bubble-chart')
