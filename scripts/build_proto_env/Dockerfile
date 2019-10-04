# FROM alpine:3.10
FROM python:3.7-stretch

ENV PROTOC_VERSION 3.10.0

# RUN apk --update --no-cache add \
#         curl \
#         unzip \
#         libc6-compat \
#     && rm -rf /var/cache/apk/*

RUN apt update && \
    apt install -y \
        curl \
        unzip \
    && rm -rf /var/lib/apt/lists/*

# Install protobuf
RUN mkdir -p /protobuf && \
    curl -L https://github.com/protocolbuffers/protobuf/releases/download/v3.10.0/protoc-${PROTOC_VERSION}-linux-x86_64.zip > /tmp/protobuf.zip && \
    unzip /tmp/protobuf.zip -d /protobuf && \
    rm -f /tmp/protobuf.zip

# Install protobuf-plugin for mypy stub files
RUN pip3 install mypy-protobuf

RUN mkdir -p /import
WORKDIR /import

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
