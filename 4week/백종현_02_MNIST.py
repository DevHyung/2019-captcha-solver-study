from tensorflow.examples.tutorials.mnist import input_data   #tensorflow샘플에 포함된 예제
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)   #학습데이터 다운로드, one hot방식으로 데이터를 처리하겠다.
# #one-hot벡터는 하나의 차원만 1이고 나머지 모든 차원들은 0으로 채원진 벡터
# 3 -> [0,0,0,1,0,0,0,0,0,0]
# 데이터 갯수가 늘어날수록 벡터의 크기가 계속늘어난다. 데이터가 많을경우 비효율적임
# tensorflow 라이브러리 추가
import tensorflow as tf
'''
softmax
입력이 특정 클래스에 해당되는지 증거를 더하고, 증거 계산을 위해 픽셀 농도의 가중치합을 이용
증거를 확률로 변환한다.
입력값을 출력으로 0~1사이의 값으로 정규화
출력들의 총합은 항상 1
(0.9, 0.8, 0.7) 출력의 절댓값은 높지만  
위보다  (0.6, 0.3, 0.1)이 구분하기 쉬움
0~9에 대한 확률분포를 얻자
'''
#변수 설정
x = tf.placeholder(tf.float32, [None, 784]) # None은 어떤 길이도 될수 있음, 28X28 pixel
W = tf.Variable(tf.zeros([784, 10]))  # 가중치값 변수
b = tf.Variable(tf.zeros([10]))  # 편향값 변수
y = tf.nn.softmax(tf.matmul(x, W) + b)  # matmul 곱하기, 소프트맥스 회귀로 모델 만들기 y=sorfmax(Wx+b)

'''
모델을 학습시킬때, 무엇이 좋은지 나쁜지 정의가 필요함
비용(cost) 소실(loss)를 최소화 하려고 시도
괜찮은 비용함수 중 하나가 cross-entropy
이 값이 낮을수록 좋은 모델
'''
# cross-entropy 모델을 설정
'''
y: 예측한 확률분포
y_: 실제분포(입력할 one-hot벡터)
수식 설명
sum: 본 모든 이미지들에 대한 교차 엔트로피의 합, 모든 차원이 제거되고 하나의 스칼라 값
'''
y_ = tf.placeholder(tf.float32, [None, 10])  # 새 placeholder 추가, 숫자 0~9
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
'''
tensorflow는 계산과정의 전체 그래프를 알고 있어, 비용 최소화에 어떤 변수가
얼마나 영향을 주는지 효율적으로 계산한다. 
cross-entropy(비효율정도)를 최소화하는 방향으로 최적화 하는 방법은 여러가지가 있지만 
경사하강법(gradient descent) 방법을 이용
경사 하강법: 각각의 변수들을 비용은 줄이는 방향으로 조금씩 바꾸는 방법
손실을 줄이기위해 함수의 그래프상(y축 손실) 최소값을 찾기위해 기울기의 반대방향으로 이동
학습도(tensor or floating point value)를 0.01를 주고 경사하강법알고리즘을 이용하여 교차 엔트로피를 최소화한다.
'''
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
# 학습을 위한 모델 준비 끝

# 만든 변수들을 초기화하고 세션에서 모델을 시작한다.
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# 1000번을 학습시킨다.
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)  # 학습세트에서 100개의 무작위 데이터들의 일괄처리(batch)를 가져옴
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})  # 이미지, 라벨

# 학습된 모델이 얼마나 정확한지를 출력
'''
tf.argmax는 특정축을 따라 가장 큰 원소의 인덱스 알려줌
tf.equal예측이 실제와 맞았는지 bool리스트 반환
'''
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))  #실제와 맞았는지?
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  #  타입 캐스트하고, 모든 차원이 제거되고 하나의 스칼라값 평균
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  # 테스트 이미지와 라벨을 넣고 정확도 테스트