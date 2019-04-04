---
title: 03_Hexo
date: 2019-04-04 16:43:01
tags: Hexo
categories: Hexo
---
### 1. Tag Plugins

---

Hexo는 마크다운 외에 포스트를 작성하기 위해 Tag Plugin이라는 자체적인 문법을 지원

#### 1.1 인용 구문
---
**How to use**
```
{% blockquote [author[, source]] [link] [source_link_title] %}
content
{% endblockquote %}
```
**Example**
```
{% blockquote 신동욱, 대학원생 https://github.com/nawook96 %}
배고프다
{% endblockquote %}
```
**Result**
{% blockquote 신동욱, 대학원생 https://github.com/nawook96 %}
배고프다
{% endblockquote %}

#### 1.2 코드 삽입
---
lang은 https://highlightjs.org 에서 지원하는 언어만 나옴(highlight), 파일명 명시도 가능
**How to use**
```
{% codeblock [title] [lang:language] [url] [link text] %}
code snippet
{% endcodeblock %}
```
**Example**
```
{% codeblock lang:objc hi.h%}
[rectangle setX: 10 y: 10 width: 20 height: 20];
{% endcodeblock %}
```
**Result**
{% codeblock lang:objc hi.h%}
[rectangle setX: 10 y: 10 width: 20 height: 20];
{% endcodeblock %}

#### 1.3 YOUTUBE 삽입
---
**How to use**
```
{% youtube video_id %}
```
**Example**
```
{% youtube Z0ti3pBKmes %}
```
**Result**
{% youtube Z0ti3pBKmes %}

#### **1.4 Asset 삽입**
----
이미지 삽입에서 추가 설명
**How to use**
```
{% asset_path slug %}
{% asset_img slug [title] %}
{% asset_link slug [title] %}
```

### 2. disqus 추가하기

---

1. disqus 가입하기
2. I want to comment on site 클릭
3. edit profile -> Acount에서 username 설정하기
4. <https://disqus.com/profile/signup/intent/> I want to install Disqus on my site 클릭 & 설정
5. hexo 폴더의 _config.yml 편집

```
disqus_shortname: username
```

+ disqus site를 만들 때 한국어 설정이 안보이는경우가 있습니다. 
+ 이때는 개발자 도구를 열어 수정하면 사용가능합니다.

![캡처](https://user-images.githubusercontent.com/36959292/55462622-27f17580-5632-11e9-9890-4f4b5191cee5.PNG)

+ 맨 마지막 줄 추가!

### 3. Hexo Blog에 image 추가

---

hexo는 source 폴더의 자원을 가지고 generate를 할 때 public 폴더를 생성합니다.

+ 전역자원 폴더(/source)

/source/images라는 폴더를 사용하면 어느 포스트던 폴더 내 자원사용이 가능합니다.



+ 포스트 자원 폴더

전역 폴더에서 모든 파일을 관리하는 것이 아니라 포스트마다 폴더를 만들어 관리할 수 있습니다.

```
# Writing
post_asset_folder: true
```

hexo 블로그 폴더의 _config.yml에서 위와 같이 변경하면 

```shell
hexo new 
```

를 할때마다 폴더가 함께 생성됩니다.



```
![](./folder/img.png)
```

전역자원 폴더에 비해 상대경로로 빠르게 접근 가능하다는 장점이 있습니다.

#### 3.1 Asset을 이용하여 image 추가
---
{% asset_img cap1.PNG [cap1] %}
```
hexo new post "blahblah"
```
다음 명령 실행시 같은 경로에 blahblah 폴더가 같이 생성됨
{% asset_img cap2.PNG [cap2] %}
**Example**
```
{% asset_img cap1.PNG [cap2] %}
```
**Result**
{% asset_img cap1.PNG [result1] %}

{% asset_img cap3.PNG [cap3] %}
{% asset_img cap4.PNG [cap4] %}
```
[📃 PDF FILE ](../pdf/Git.pdf)
{% asset_link Git.pdf 📃 PDF FILE %}
```
**어떻게 다를까?**
{% asset_img cap5.PNG [cap5] %}
{% asset_img cap6.PNG [cap6] %}
위에 사용한건 상대경로이기 때문에 Home 화면을 제외한 곳에서 포스트를 보게 되면 찾을 수가 다.