FROM alpine:3.17

RUN apk add --no-cache \
    wget \
    unzip \
    git \
    python3

RUN mkdir /workspace
WORKDIR /workspace

COPY scripts ./scripts/
COPY notebooks ./notebooks/
COPY download_dataset.sh .

RUN sh download_dataset.sh

RUN apk add --no-cache \
    py3-nltk \
    py3-numpy \
    py3-pandas \
    py3-scipy \
    py3-matplotlib \
    py3-pillow

RUN mkdir -p /root/nltk_data/
RUN git clone https://github.com/nltk/nltk_data.git
RUN mv nltk_data/packages/* /root/nltk_data/
RUN rm -rf nltk_data/

RUN cd /root/nltk_data/tokenizers/ && \
    unzip punkt.zip && \
    rm punkt.zip
