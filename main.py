from tester import test_algorithm
import plot_results
import sortingalgs


def main():
  #print(sortingalgs.merge_sort([5, 3, 12, 52, 323]))
  test_algorithm(sortingalgs.bogo_sort, "bogosort")
  plot_results.plotcsv("bogosort")

if __name__ == '__main__':
  main()

