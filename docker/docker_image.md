# 도커 이미지 만들기

### 1. 도커 이미지 실행

도커의 이미지는 Base Image로 부터 만들어진다. 우리는 Ubuntu를 os로 할 것이므로 os 이미지를 받아본다.

```
$ sudo docker pull ubuntu
```

이미지가 있는지 확인해보고 이미지를 컨테이너에 실행시켜보자.

```
$ sudo docker run -t -i ubuntu /bin/bash
```

![1560838428284](/home/jungeun/.config/Typora/typora-user-images/1560838428284.png)

잘 실행이 되면 빠져나온다.



### 2. Dockerfile로 이미지 생성

우선 간단하게 c언어로 hello_world.c프로그램을 작성하고 빌드한다. (실행파일 이름은 helloworld)

Dockerfile 작성

```
FROM ubuntu
MAINTAINER jungeun9729@gmail.com

ADD helloworld helloworld
RUN chmod 755 helloworld
CMD ["./helloworld"]
```

FROM : base image 지정

ADD : 로컬의 helloworld를 이미지에 helloworld란 이름으로 복사

RUN : 실행을 위해 helloworld의 권한을 변경

CMD : helloworld실행파일 실행



그럼 이미지를 빌드해본다.

```
$ sudo docker build -t helloworld .
```

![1560841451020](/home/jungeun/.config/Typora/typora-user-images/1560841451020.png)

그럼 위와 같이 한줄씩 실행하며 이미지를 만든다는 것을 확인할 수 있고  ```docker images```명령어로 성공적으로 이미지가 생성되었음을 확인한다. 



### 3. 이미지 실행

그럼 이미지를 컨테이너에 올려 실행해본다.

```
$ sudo docker run helloworld
```

![1560841653983](/home/jungeun/.config/Typora/typora-user-images/1560841653983.png)

![1560841701686](/home/jungeun/.config/Typora/typora-user-images/1560841701686.png)



컨테이너는 helloworld를 실행하고 종료되어도 유지되어 있다. 그래서 이미지를 지우려고 ```sudo docker rmi helloworld```를 하면 컨테이너에 참조되어 있는 이미지라 지울 수 없다고 뜬다. 그래서 컨테이너와 이미지를 함께 지우기 위해 f 옵션을 주어서 ```sudo docker rmi -f helloworld```를 하면 된다.

그래서 컨테이너가 종료된 즉시 삭제되게 하기 위해  run할 때 --rm 옵션을 주면 된다.