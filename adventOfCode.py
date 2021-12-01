
def findDepth(x):
    x = [int(i) for i in x.readlines()]
    prev = x[0]
    for i in x:
        if prev == i:
            print(f'{i} (N/A - no previous measurement')
            count = 0
        else:
            if prev > i:
                print(f'{i} (decreased)')
            if prev < i:
                print(f'{i} (increased)')
                count += 1
        prev = i

    return count

def threeMeasSlideWin(x):
    prevSum, currSum = 0, 0
    arr = [int(i) for i in x.readlines()]
    i = 0

    while i < len(arr)-2:
        currSum = arr[i] + arr[i+1] + arr[i+2]
        if prevSum == 0:
            print(f'{currSum} (N/A - no previous measurement')
            count = 0
        else:
            if currSum > prevSum:
                print(f'{currSum} (increased)')
                count += 1
            if currSum < prevSum:
                print(f'{currSum} (decreased)')
        prevSum = currSum
        i += 1
    return count

def main():
    val = open('input.txt')
    depthArr = findDepth(val)
    print(depthArr)
    val = open('input.txt')
    print(threeMeasSlideWin(val))

if __name__ == "__main__":
    main()