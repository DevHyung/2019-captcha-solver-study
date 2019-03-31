# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

__author__ = "youhyeoneee(김유현)"
#출처 : http://pythonstudy.xyz/python/article/408-pandas-%EB%8D%B0%EC%9D%B4%ED%83%80-%EB%B6%84%EC%84%9D
'''
Panel 기초 
'''
#아래 예제는 numpy를 사용하여 3차원 난수를 발생시킨 후,
# 이를 pandas.Panel() 에 적용한 예이다.
# 출력 결과에 보면,
# 2 (items) x 3 (major_axis) x 4 (minor_axis) 크기의 Panel 객체가 생성되었음을 알 수 있다.
# Panel 객체 p로부터 p[0]을 조회하면,
# Axis 0 의 첫번째 요소인 DataFrame이 출력됨을 볼 수 있다.

data = np.random.rand(2,3,4)
p = pd.Panel(data)
print(p)

print(p[0])
print(p[1])