
# Adapted from knapsack implementation in lectures
def shoppingSpree(W, wt, val, n): 
    OPT = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build OPT table
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                OPT[i][w] = 0
            elif wt[i-1] <= w: 
                if val[i-1] + OPT[i-1][w-wt[i-1]] > OPT[i-1][w]:
                    OPT[i][w] = val[i-1] + OPT[i-1][w-wt[i-1]]
                else:
                    OPT[i][w] = OPT[i-1][w]
            else: 
                OPT[i][w] = OPT[i-1][w]
    # return the OPT
    return OPT
    
    
def results(W, wt, val, n, OPT, filename, testCase):     
    with open(filename, "a+") as outFile:
        outFile.write("Test Case %i\n" % testCase)

        outFile.write("Total price %i\n" %sum(OPT[-1]))
        outFile.write("Member items: \n")
        
        counter = 1
        for w in W:
            res = OPT[n][w] 
            outFile.write("%i : " %counter)
            
            counter+=1
            for i in range(n, 0, -1): 
                if res <= 0: 
                    break
                if res == OPT[i - 1][w]: 
                    continue
                else: 
                    # This item is included. 
                    outFile.write("%i " %i)
                    
                    res = res - val[i - 1] 
                    w = w - wt[i - 1]
            outFile.write("\n")
        outFile.close()

def readInFile(filename, val, wt, W):
    inFile = open(filename, "r")
    T = int(inFile.readline())
    for i in range(T):
        P = []
        Wi = []
        M = []
        N = int(inFile.readline())
        for j in range(N):
            line = inFile.readline()
            arr = line.strip().split(" ")
            P.append(int(arr[0]))
            Wi.append(int(arr[1]))
        val.append(P)
        wt.append(Wi)
        F = int(inFile.readline())
        for k in range(F):
            M.append(int(inFile.readline()))
        W.append(M)
    inFile.close()
    


if __name__ == '__main__':
    val = []
    wt = []
    W = []
    filename = "shopping.txt"
    readInFile(filename, val, wt, W)

    shops = len(val)

    outFile = "result.txt"

    for i in range(shops):
        curVal = val[i]
        curWt = wt[i]
        curW = W[i]
        n = len(curVal) 
        OPT = shoppingSpree(max(curW) , curWt , curVal , n) 
        results(curW, curWt, curVal, n, OPT, outFile, i+1)

        
