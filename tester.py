import random
from time import perf_counter

def swap(mylist, i, j):
  temp = mylist[j]
  mylist[j] = mylist[i]
  mylist[i] = temp

def scramble(mylist, n):
  list_len = len(mylist)
  for _ in range(n):
      i = random.randrange(list_len)
      j = random.randrange(list_len)
      swap(mylist, i, j)

def generaterandlist(size):
  numlist = []
  for y in range(0, size, 1):
    numlist.append(y)
  random.shuffle(numlist)
  return numlist

def generatereverselist(size):
  numlist = []
  for y in range(size, 0, -1):
    numlist.append(y)
  return numlist

def generateshuffledlist(size, shuffleamt):
  numlist = []
  for y in range(0, size, 1):
    numlist.append(y)
  scramble(numlist, shuffleamt)
  return numlist

def time_Exec(num_iters, func, *args, **kwargs):
  sort_times = []
  result = None
  for _ in range(num_iters):
    start_time = perf_counter()
    result = func(*args, **kwargs)
    end_time = perf_counter()
    sort_times.append(end_time-start_time)
  return sum(sort_times)/num_iters, result


#####################
def test_algorithm(sortfunc, outfilename,
            trials = 1, scrambleamt = 5, start = 1, end = 10, step = 1 ):
  file = open(outfilename, "w")
  file.write("size,random,reversed,shuffled")
  for cursize in range(start, end + step, step):
    file.write("\n")
    #generate lists
    randlist = generaterandlist(cursize)
    reverselist = generatereverselist(cursize)
    shuffledlist = generateshuffledlist(cursize, scrambleamt)
    #test lists
    randtime, randresult = time_Exec(trials, sortfunc, randlist)
    reversetime, reverseresult = time_Exec(trials, sortfunc, reverselist)
    shuffledtime, shuffledresult = time_Exec(trials, sortfunc, shuffledlist)
    #add to file
    string = "{},{},{},{}".format(cursize, randtime, reversetime, shuffledtime)
    file.write(string)
    print(cursize)
  file.close()

