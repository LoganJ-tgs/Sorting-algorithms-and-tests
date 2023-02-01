import matplotlib.pyplot as plt
import pandas as pd

def plotcsv(csvname, xlabel = 'size', ylabel = 'Runtime, seconds'):
  data = pd.read_csv(csvname)

  plt.figure(figsize=(8,6))
  plt.plot(data['size'], data['random'], label='random list')
  plt.plot(data['size'], data['reversed'], label='reversed list')
  plt.plot(data['size'], data['shuffled'], label='shuffled list')

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid()
  plt.legend()
  plt.savefig(csvname.strip(".csv") + '.png')



"""
def main():
    expt_data = pd.read_csv('bubble_sort_results_rand.csv')
    expt_data2 = pd.read_csv('bubble_sort_results_opp.csv')
    expt_data3 = pd.read_csv('bubble_sort_results_almsort.csv')

    plt.figure(figsize=(8,6))
    plt.plot(expt_data['size'], expt_data['time'], label='random list')
    plt.plot(expt_data2['size'], expt_data2['time'], label='opposite list')
    plt.plot(expt_data3['size'], expt_data3['time'], label='almost sorted list')
    #plt.plot(expt_data['exponent'], expt_data['min_runtime_builtin'], label='Builtin Method')
    plt.xlabel('list size')
    plt.ylabel('Runtime, seconds')
    plt.grid()
    plt.legend()
    plt.savefig('new_runtime.png')
    #plt.show()
    """