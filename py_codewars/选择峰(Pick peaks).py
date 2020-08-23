def pick_peaks(arr):
    d = {'pos':[],'peaks':[]}
    for i in range(1,len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            d['pos'].append(i)
            d['peaks'].append(arr[i])
        elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
            for j in range(i+2,len(arr)):
                if arr[j] < arr[i]:
                    d['pos'].append(i)
                    d['peaks'].append(arr[i])
                    break
                elif arr[j] != arr[i]:
                    i = j
                    break
    return d
print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))