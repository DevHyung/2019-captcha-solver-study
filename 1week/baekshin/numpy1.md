## 1. numpy

+ numpy는 과학계산을 위한 라이브러리 

+ 다차원 배열을 처리하는데  유용한 기능을 제공

+ 리스트나 튜플보다 훨씬 더 빨리 배열을 처리



## 2. 배열만들기(1):array()

+ 리스트와 튜플로부터 배열 생성가능

```python
a = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print(a.ndim) #랭크 반환 2
print(a.size) #배열에 있는 총 개수 반환 8
print(a.shape) #각 차원의 크기 반환 (2,4)
```



## 3. 배열만들기(2):arange()

```python
b = np.arange(10) #[0 1 2 3 4 5 6 7 8 9]
b= np.arange(7, 10) #[7 8 9]
b = np.arange(0, 10, 2) #[0 2 4 6 8]
b = np.arange(2.0, 3.0, 0.3) #[2.  2.3 2.6 2.9]
```



## 4. 배열만들기(3):zeros(), ones(), random()

+ zeros() : 모든 값이 0인 배열 반환

```python
c = np.zeros((2, 4))
```

[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]



+ ones() : 모든 값이 1인 배열 반환

```python
c = np.ones((3, 3))
```

[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]



+ random() : 0.0과 0.1 사이의 임의 값을 채운 배열 반환

```python
c = np.random.random((2, 4))
```

[[0.89451067 0.46158826 0.32610563 0.20057699]
 [0.58088544 0.93966855 0.23445485 0.72952238]]



## 5. 배열 모양 바꾸기 : reshape()

+ 배열의 랭크 크기의 곱이 총 배열 수와 같아야 함

```python
d = np.arange(0,10)
d = d.reshape(2,5)
```

[[0 1 2 3 4]
 [5 6 7 8 9]]



## 6. 항목 얻기 : []

+ 1차원 배열은 리스트처럼 작동

```python
e = np.arange(0,10)
print(e[-1], e[7]) #9 7
```

 

+ 2차원은 리스트와 다르다

```python
e.shape= (2,5)
print(e[1,1])
e = [[0,1,2],[3,4,5]]
print(e[1,1]) #에러 발생
```



## 7. 배열 연산

+ 더하기, 빼기, 곱하기 동시연산 가능

```python
from numpy import *
a = arange(0,3) #[0 1 2]
a *= 3 #[0 3 6]
```

 

+ @ : 행렬곱

```python
a= np.array([[1,2],[3,4]])
b = a@a
```



## 8. 실습

+ 랜덤 분포 생성
+ 파일 입출력

```python
mean = 0 #평균
std = 5 #표준편차
arr1 = np.random.normal(mean, std, [5, 5]) #정규분포
arr2 = np.random.exponential(2, [5, 5]) #지수분포
arr3 = arr1 * arr2
print(arr3)
np.save("./data", arr3) #data.npy로 저장

arr = np.load("./data.npy") #불러오기
devArr = np.vsplit(arr, 5) #가로로 자르기
print(devArr[0][0])
plt.plot(devArr[0][0]) #그래프그리기
plt.show()
```



+ 결과

![hi](./Figure_1.png)





