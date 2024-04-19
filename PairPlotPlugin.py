import matplotlib.pyplot as plt
import seaborn as sns
import pandas

class PairPlotPlugin:
 def input(self, inputfile):
  self.df = pandas.read_csv(inputfile)
 def run(self):
  sns.pairplot(self.df, hue='day')
 def output(self, outputfile):
   plt.savefig(outputfile)
