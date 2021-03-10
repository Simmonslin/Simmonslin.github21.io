import numpy as np

ans1=20*(np.log10(20000/20))
print("20000微斯巴卡 = %d 分貝" %(ans1))

upa30=(30+20*(np.log10(20)))/20

upa50=(50+20*(np.log10(20)))/20


print("30分貝聲押為50分貝的 %.4f倍" %(upa30/upa50))
