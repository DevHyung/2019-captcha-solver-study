# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
#출처: https://doorbw.tistory.com/172 [Tigercow.Door]

df = pd.DataFrame(np.random.randn(6,4))
print(df)

df.columns = ['A', 'B', 'C', 'D']
df.index = pd.date_range('20160701', periods=6)
#pandas에서 제공하는 date range함수는 datetime 자료형으로 구성된, 날짜 시각등을 알 수 있는 자료형을 만드는 함수
print(df.index)

print(df)

# np.nan은 NaN값을 의미한다.
df['F'] = [1.0, np.nan, 3.5, 6.1, np.nan, 7.0]
print(df)

##NaN없애기
# 행의 값중 하나라도 nan인 경우 그 행을 없앤다.
print(df.dropna(how='any'))

# 행의 값의 모든 값이 nan인 경우 그 행으 없앤다.
print(df.dropna(how='all'))

'''
주의 drop함수는 특정 행 또는 열을 drop하고난 DataFrame을 반환한다.

즉, 반환을 받지 않으면 기존의 DataFrame은 그대로이다.

아니면, inplace=True라는 인자를 추가하여, 반환을 받지 않고서도

기존의 DataFrame이 변경되도록 한다.
'''

# nan값에 값 넣기
print(df.fillna(value=0.5))

# nan값인지 확인하기
print(df.isnull())

# F열에서 nan값을 포함하는 행만 추출하기
print(df.loc[df.isnull()['F'],:])

print(pd.to_datetime('20160701'))

# 특정 행 drop하기
print(df.drop(pd.to_datetime('20160701')))

# 2개 이상도 가능
print(df.drop([pd.to_datetime('20160702'),pd.to_datetime('20160704')]))

# 특정 열 삭제하기
print(df.drop('F', axis = 1))

# 2개 이상의 열도 가능
print(df.drop(['B','D'], axis = 1))




