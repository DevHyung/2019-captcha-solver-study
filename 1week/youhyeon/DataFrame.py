# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

#출처 : https://doorbw.tistory.com/172

# Data Frame 정의하기
# 이전에 DataFrame에 들어갈 데이터를 정의해주어야 하는데,
# 이는 python의 dictionary 또는 numpy의 array로 정의할 수 있다.
data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
        'year': [2013, 2014, 2015, 2016, 2015],
        'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df)
#행과 열의 구조를 가진 데이터가 생긴다

#행 방향의 index
print(df.index)
#열 방향의 index
print(df.columns)
#값 얻기
print(df.values)
#각 인덱스에 대한 이름 설정하기
df.index.name = 'Num'
df.columns.name = 'Info'
print(df)

#DataFrame을 만들면서 columns와 index를 설정할 수 있다.
df2 = pd.DataFrame(data, columns=['year', 'name', 'points', 'penalty'], index=['one', 'two', 'three', 'four', 'five'])

print(df2)

'''
DataFrame을 정의하면서, data로 들어가는 python dictionary와 columns의 순서가 달라도 알아서 맞춰서 정의된다.

하지만 data에 포함되어 있지 않은 값은 NaN(Not a Number)으로 나타나게 되는데,

이는 null과 같은 개념이다.

NaN값은 추후에 어떠한 방법으로도 처리가 되지 않는 데이터이다.

따라서 올바른 데이터 처리를 위해 추가적으로 값을 넣어줘야 한다.
'''

# describe() 함수는 DataFrame의 계산 가능한 값들에 대한 다양한 계산 값을 보여준다.

print(df2.describe())