FROM dorowu/ubuntu-desktop-lxde-vnc:bionic
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && yes | apt-get install python3.7 \
 && yes | apt-get install git
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 10
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
RUN yes| apt-get install python3 python-dev python3-dev python3.7-dev\
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev \
     python-pip
COPY . /
RUN cd / && chmod +x prepare.sh && ./prepare.sh 
CMD cd / && python3 recognition.py

