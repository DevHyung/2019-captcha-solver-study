# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

__author__ = "youhyeoneee(김유현)"
#출처: https://doorbw.tistory.com/172 [Tigercow.Door]

'''
DataFrame indexing 관련  
'''
data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])
print(df)

print(df['year']) # df.year도 됨

# 특정 열에 대해 위와 같이 선택하고, 우리가 원하는 값을 대입할 수 있다.
df['penalty'] = 0.5
print(df)
# 또는
df['penalty'] = [0.1, 0.2, 0.3, 0.4, 0.5] # python의 List나 numpy의 array
print(df)

#새로운 열을 추가하기
df['zeros'] = np.arange(5)
print(df)

# Series를 추가할 수도 있다.
val = pd.Series([-1.2, -1.5, -1.7], index=['two','four','five'])
df['dept'] = val
print(df)
'''
하지만 Series로 넣을 때는 val와 같이 넣으려는 data의 index에 맞춰서 데이터가 들어간다.

이점이 python list나 numpy array로 데이터를 넣을때와 가장 큰 차이점이다.

'''

df['net_points'] = df['points'] - df['penalty']
df['high_points'] = df['net_points'] > 2.0
print(df)

# 열 삭제하기
del df['high_points']
del df['net_points']
del df['zeros']
print(df)

print(df.columns)

df.index.name = 'Order'
df.columns.name = 'Info'
print(df)


#####################DataFrame에서 행을 선택하고 조작하기
# 0번째 부터 2(3-1) 번째까지 가져온다.
# 뒤에 써준 숫자번째의 행은 뺀다.
print(df[0:3])

# tow라는 행부터 four라는 행까지 가져온다.
# 뒤에 써준 이름의 행을 빼지 않는다.
print(df['two':'four']) # 하지만 비추천!

# 아래 방법을 권장한다.
# .loc 또는 .iloc 함수를 사용하는 방법.
print(df.loc['two']) # 반환 형태는 Series

print(df.loc['two':'four'])

print(df.loc['two':'four','points']) #two에서 four까지 points만

print(df.loc[:,'year']) #==df['year']

print(df.loc[:,['year','names']])

print(df.loc['three':'five','year':'penalty']) #three부터 five까지에서 year부터 penalty를 가져옴

# 새로운 행 삽입하기
df.loc['six',:] = [2013,'Jun',4.0,0.1,2.1]
print(df)

# .iloc 사용:: index 번호를 사용한다.
print(df.iloc[3]) # 3번째 행을 가져온다.

print(df.iloc[3:5, 0:2])

print(df.iloc[[0,1,3], [1,2]])

print(df.iloc[:,1:4])

print(df.iloc[1,1])

#######################Boolean Indexing

print(df)

# year가 2014보다 큰 boolean data
print(df['year'] > 2014)

# year가 2014보다 큰 모든 행의 값
print(df.loc[df['year']>2014,:])

print(df.loc[df['names'] == 'Kilho',['names','points']])

# numpy에서와 같이 논리연산을 응용할 수 있다.
print(df.loc[(df['points']>2)&(df['points']<3),:])

# 새로운 값을 대입할 수도 있다.
df.loc[df['points'] > 3, 'penalty'] = 0
print(df)


