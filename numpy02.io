import numpy as np

print("1.")

ans1=np.array(range(30)).reshape(5,6)

print(ans1)

print()


print("2.")

ans2=np.array(ans1,order="F")

print(ans2[ans2%6==1])

