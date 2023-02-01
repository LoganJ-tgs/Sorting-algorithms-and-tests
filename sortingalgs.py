def swap(mylist, i, j):
  temp = mylist[j]
  mylist[j] = mylist[i]
  mylist[i] = temp

def isSorted(mylist):
  for i in range(len(mylist)-1):
    if mylist[i]>mylist[i+1]:
      return False
  return True

# algoritms
def bubble_sort(mylist):
  while not isSorted(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
          swap(mylist, i, i+1)


def insertion_sort(mylist):
  # for all items in list
  for i in range(len(mylist)):
    hasswapped = False
    val = mylist[i]
    # move backwards until you get something larger or same size
    for x in range(i - 1, 0, -1):
      if mylist[x] <= val:
        # swap
        mylist.insert(x+1, mylist.pop(i))
        hasswapped = True
        break
    # if there was nothing larger or same size then put it at the front
    if not hasswapped:
      mylist.insert(0, mylist.pop(i))

def merge_sort(mylist):
  totallen = len(mylist)
  # if the list is length of 1 then return
  if totallen == 1:
    return mylist
  # else then sort
  else:
    #split the list and merge sort those
    midindex = totallen // 2
    leftlist = merge_sort(mylist[:midindex])
    rightlist = merge_sort(mylist[midindex:])

    lindex, rindex = 0, 0
    lenleft = len(leftlist)
    lenright = len(rightlist)
    sortedlist = []
    #combine the lists
    while True:
      #compare first items, then append the lower one
      if leftlist[lindex] < rightlist[rindex]:
        sortedlist.append(leftlist[lindex])
        lindex += 1
      else:
        sortedlist.append(rightlist[rindex])
        rindex += 1

      # if one of he indexes = len(list) then add the other list and return
      if lindex == lenleft:
        return sortedlist + rightlist[rindex:]
      elif rindex == lenright:
        return sortedlist + leftlist[lindex:]
      """
      if lindex == lenleft:
        for x in range(rindex, lenright, 1):
          sortedlist.append(rightlist[x])
        return sortedlist
      elif rindex == lenright:
        for x in range(lindex, lenleft, 1):
          sortedlist.append(leftlist[x])
        return sortedlist
      
      """
      


import random
def bogo_sort(mylist):
  while not isSorted(mylist):
    random.shuffle(mylist)
  return mylist