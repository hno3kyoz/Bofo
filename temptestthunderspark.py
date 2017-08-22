import thunder as td
import matplotlib.pyplot as plt
import seaborn as sns
print('point 2')
series = td.series.fromexample('fish')
print('download finish')
sns.set_style('darkgrid')
sns.set_context('notebook')
print('sns finish')
examples = series.filter(lambda x: x.std() > 6).normalize().sample(100).toarray()
print('example down start to plot')
plt.plot(series.index, examples.T)
