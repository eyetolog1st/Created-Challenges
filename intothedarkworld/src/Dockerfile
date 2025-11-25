FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update --fix-missing && apt install libseccomp-dev python3 python3-pip socat -y

RUN groupadd -r ctf && useradd -r -g ctf ctf

RUN pip install pycrypto pycryptodome --break-system-packages

ENV TERM=linux
ENV TERMINFO=/etc/terminfo

WORKDIR /home/ctf

COPY question.py .


RUN chmod 550 /home/ctf/question.py

RUN echo '#!/bin/bash' > /home/ctf/run \
    && echo 'cd /home/ctf && exec python3 question.py' >> /home/ctf/run
RUN chmod 750 /home/ctf/run

RUN chown -R root:ctf /home/ctf

EXPOSE 3456

CMD socat TCP-L:3456,fork EXEC:"/home/ctf/run",reuseaddr,stderr