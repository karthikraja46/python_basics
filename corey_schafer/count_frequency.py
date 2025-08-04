arr=[1,2,3,3,4,5,5,6]

n= len(arr)

vis=[False for i in range(100)]

for i in range(n):
    if vis[i]==False:
        count=1
        vis[i]=True
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
                vis[j]=True
        print(arr[i],"->",count)