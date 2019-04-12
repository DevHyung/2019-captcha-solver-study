import  tensorflow as tf
__author__ = "youhyeoneee(김유현)"
#출처
# https://post.naver.com/viewer/postView.nhn?volumeNo=17146229&memberNo=1085064&navigationType=push
# https://www.youtube.com/watch?v=-57Ne86Ia8w&feature=youtu.be
#그래프 생성
#그래프 노드를 정의하고 출력합니다.

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) #also th.float32 implicity
node3 = tf.add(node1, node2) # <=> node3 = node1+ node2

print("node1 : ", node1, "node2 : ", node2)
print("node3 : ", node3)

# 그래프 실행
sess = tf.Session()
print("sess.run(node1, node2) : ", sess.run([node1, node2]))
print("sess.run(node3):", sess.run(node3))

sess.close()