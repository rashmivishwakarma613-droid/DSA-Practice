arr=list(map(int,input("\nenter arry").split()))
curr_sum=arr[0]
max_sum=arr[0]
for i in range(1,len(arr)):
    curr_sum=max(arr[i],curr_sum+arr[i])
    max_sum= max(max_sum,curr_sum)

    
    
print("sum",max_sum)
