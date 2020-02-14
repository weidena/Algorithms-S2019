import time
import random

def first_fit(arr, C):
    bins = [0]
    for element in arr:
        j = 0
        for w in bins:
            if w+element <= C:
                bins[j] = w+element
                break
            j+=1
        if j == len(bins):
            bins.append(element)
    return len(bins)

def best_fit(arr, C):
    bins = [0]
    for element in arr:
        j = 0
        weights = [0]*len(arr)
        for w in bins:
            if w+element <= C:
                weights[j] = w
            else:
                weights[j] = -1
            j+=1
        ind = weights.index(max(weights))
        if ind >= len(bins):
            bins.append(element)
        else:
            bins[ind] += element
    return len(bins)

def fillArray(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1,10))
    return arr

if __name__ == '__main__':
    items = [10, 50, 500, 1000, 1500, 2000, 5000, 10000, 20000]
    arr = []
    for item in items:
        arr.append(fillArray(item))
    i = 0
    print(arr)
    for row in arr:
        C = 50
        start1 = time.time()
        num_bins_first = first_fit(row, C)
        start2 = time.time()
        num_bins_best = best_fit(row, C) 
        start3 = time.time()
        row.sort(reverse = True)
        num_bins_dec = first_fit(row, C) 
        end = time.time()      
        
        print("Test Case %i" %(i+1))
        print("First-Fit: %i\t" %num_bins_first),
        print("Time: %f\t" %(start2-start1))
        print("First-Fit-Decreasing: %i\t" %num_bins_dec),
        print("Time: %f" %(start3-start2))
        print("First-Best: %i\t" %num_bins_best),
        print("Time: %f\n" %(end-start3))
            

        i+=1


"""arr = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
C = 10
num_bins = first_fit(arr, C)
print(num_bins)
num_bins = best_fit(arr, C)
print(num_bins)

arr.sort(reverse = True)
num_bins = first_fit(arr, C)
print(num_bins)"""
