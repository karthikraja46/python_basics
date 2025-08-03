
s=3
e=10
prime_num_count=0

for i in range(s,e+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        prime_num_count+=1

print(prime_num_count)
        