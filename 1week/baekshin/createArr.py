import numpy as np
import matplotlib.pyplot as plt


t = np.array([[1,2],[3,4]])
print(np.vsplit(t,2))#
exit(-1)
mean = 0 #평균
std = 5 #표준편차
arr1 = np.random.normal(mean, std, [5, 5]) #정규분포
arr2 = np.random.exponential(2, [5, 5]) #지수분포
arr3 = arr1 * arr2
print(arr3)
np.save("./data", arr3) # data.npy로 저장

arr = np.load("./data.npy") # 불러오기
devArr = np.vsplit(arr, 5) # 가로로 자르기
print(devArr[0][0])
plt.plot(devArr[0][0]) # 그래프그리기
plt.show()