arr = [2,4,7,9,15,18,29,35,57,85]
start = 0
end = len(arr)-1
x = int(input("Enter Key to Search : "))
while end >= start:
    mid = start + (end-1)//2
    if arr [mid] == x:
        result = mid
        break
    elif arr [mid] > x:
        end = mid - 1
    elif arr [mid] > x:
        end = mid - 1
    else:
        start = mid+1
else:
    result = -1
    
if result != -1:
    print("Element present at index "+str(result))
else:
    print("Elemnet is not present in array")
