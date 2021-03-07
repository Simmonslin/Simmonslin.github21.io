import numpy as np

ans=np.arange(0,21,1)
print(ans)


for i in ans:
    if i%2==0 and i>0:
        print(i,end=" ")

print()
  
for j in ans:
    if j%3==0 and j>0:
        print(j,end=" ")        
