# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
#출처: https://doorbw.tistory.com/172 [Tigercow.Door]

data = [[1.4, np.nan],
           [7.1, -4.5],
        [np.nan, np.nan],
        [0.75, -1.3]]
df = pd.DataFrame(data, columns=["one", "two"], index=["a", "b", "c", "d"])


print(df)

# 행방향으로의 합(즉, 각 열의 합)
print(df.sum(axis=0))

# 열방향으로의 합(즉, 각 행의 합)
print(df.sum(axis=1))

'''
이때, 위에서 볼 수 있듯이 NaN값은 배제하고 계산한다.

NaN 값을 배제하지 않고 계산하려면 아래와 같이 skipna에 대해 false를 지정해준다.

'''

print(df.sum(axis=1, skipna=False))

# 특정 행 또는 특정 열에서만 계산하기
print(df['one'].sum())

print(df.loc['b'].sum())

'''
pandas에서 DataFrame에 적용되는 함수들

sum() 함수 이외에도 pandas에서 DataFrame에 적용되는 함수는 다음의 것들이 있다.

count 전체 성분의 (NaN이 아닌) 값의 갯수를 계산

min, max 전체 성분의 최솟, 최댓값을 계산

argmin, argmax 전체 성분의 최솟값, 최댓값이 위치한 (정수)인덱스를 반환

idxmin, idxmax 전체 인덱스 중 최솟값, 최댓값을 반환

quantile 전체 성분의 특정 사분위수에 해당하는 값을 반환 (0~1 사이)

sum 전체 성분의 합을 계산

mean 전체 성분의 평균을 계산

median 전체 성분의 중간값을 반환

mad 전체 성분의 평균값으로부터의 절대 편차(absolute deviation)의 평균을 계산

std, var 전체 성분의 표준편차, 분산을 계산

cumsum 맨 첫 번째 성분부터 각 성분까지의 누적합을 계산 (0에서부터 계속 더해짐)

cumprod 맨 첫번째 성분부터 각 성분까지의 누적곱을 계산 (1에서부터 계속 곱해짐)


'''
df2 = pd.DataFrame(np.random.randn(6, 4),
                   columns=["A", "B", "C", "D"],
                   index=pd.date_range("20160701", periods=6))


print(df2)

# A열과 B열의 상관계수 구하기
print(df2['A'].corr(df2['B']))

# B열과 C열의 공분산 구하기
print(df2['B'].cov(df2['C']))

##정렬함수 및 기타함수

dates = df2.index
random_dates = np.random.permutation(dates)
df2 = df2.reindex(index=random_dates, columns=["D", "B", "C", "A"])
print(df2)

# index와 column의 순서가 섞여있다.
# 이때 index가 오름차순이 되도록 정렬해보자
print(df2.sort_index(axis=0))
# column을 기준으로?
print(df2.sort_index(axis=1))

# 내림차순으로는?
print(df2.sort_index(axis=1, ascending=False))

# 값 기준 정렬하기
# D열의 값이 오름차순이 되도록 정렬하기
print(df2.sort_values(by='D'))

# B열의 값이 내림차순이 되도록 정렬하기
print(df2.sort_values(by='B', ascending=False))

df2["E"] = np.random.randint(0, 6, size=6)
df2["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]
print(df2)

# E열과 F열을 동시에 고려하여, 오름차순으로 하려면?
print(df2.sort_values(by=['E','F']))

# 지정한 행 또는 열에서 중복값을 제외한 유니크한 값만 얻기
print(df2['F'].unique())

# 지정한 행 또는 열에서 값에 따른 개수 얻기
print(df2['F'].value_counts())

# 지정한 행 또는 열에서 입력한 값이 있는지 확인하기
print(df2['F'].isin(['alpha','beta']))
# 아래와 같이 응용할 수 있다.

# F열의 값이 alpha나 beta인 모든 행 구하기
print(df2.loc[df2['F'].isin(['alpha','beta']),:])

df3 = pd.DataFrame(np.random.randn(4, 3), columns=["b", "d", "e"],
                   index=["Seoul", "Incheon", "Busan", "Daegu"])
print(df3)

