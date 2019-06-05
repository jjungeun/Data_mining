apt-get으로 패키지를 설치하려고 할 때 종종 보던 오류이다.

```E: Could not get lock /var/lib/dpkg/lock - open (11: Resource temporarily unavailable) ```와 같은 식으로 오류가 난다.

```
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
dpkg --configure -a
```

이렇게 lock파일을 삭제하면 된다.

