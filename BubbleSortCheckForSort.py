def bubbleSort(alist):
    sorted = True
    for passnum in range(len(alist)-1,0,-1):
       for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                sorted = False            
            if sorted:
                break
    print (sorted) #had to be moved here in order to make it work on my compiler

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)