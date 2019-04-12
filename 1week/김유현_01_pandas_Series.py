# -*- coding: utf-8 -*-
import pandas as pd

'''
Serirs 기초 
'''
#Series 정의하기
obj = pd.Series([4, 'a', -5, 3])
print(obj)

#Series의 값만 확인하기
print(obj.values)

#Series의 인덱스만 확인하기
print(obj.index)

#Series의 자료형 확인하기
print(obj.dtypes)

#인덱스를 지정할 수 있다.
obj2 = pd.Series([4, 7, 5, -3], index=['a','b','c','d'])
print(obj2)

#python의 dictionary 자료형을 Series data로 만들 수 있다
#dictionary의 key가 Series의 index가 된다
sdata = {'Kim': 35000, 'Beomwoo': 67000, 'Joan': 12000, 'Choi': 4000}
obj3 = pd.Series(sdata)
print(obj3)

obj3.name = 'Salary'
obj3.index.name = "Names"
print(obj3)

#index 변경
obj3.index = ['A', 'B', 'C', 'D']
print(obj3)