
arr=list(map(int, input("enter arrr").split()))

ele=50

# arr=[10,20,30,40]
# ele=50
print("array before insertion")
for i in range(len(arr)):
    print(arr[i],end=" ")
arr.insert(0,ele)
print("\nArray after insetion")
for i in range(len(arr)):
    print (arr[i],end=" ")

    # Time Complexity: O(n), where n is the size of the array.
