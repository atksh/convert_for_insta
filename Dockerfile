FROM jrottenberg/ffmpeg

RUN  apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y python3.8 python3.8-dev python3.8-distutils \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.8 python

RUN apt-get install -y curl \
  && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python get-pip.py && rm -rf get-pip.py

WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/
ENTRYPOINT python convert.py

