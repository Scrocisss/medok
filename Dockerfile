FROM ubuntu:24.04@sha256:1e622c5f073b4f6bfad6632f2616c7f59ef256e96fe78bf6a595d1dc4376ac02

RUN apt-get -y update && apt-get -y install socat

COPY flag.txt /
RUN mv /flag.txt /flag-$(md5sum /flag.txt | awk '{print $1}').txt

RUN useradd -m ctf

USER ctf
WORKDIR /home/ctf

COPY unlock .

CMD ["socat", "tcp-l:11331,reuseaddr,fork", "exec:./unlock"]
