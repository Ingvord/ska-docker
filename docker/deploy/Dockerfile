FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y make bash git curl python-pip apt-transport-https ca-certificates wget software-properties-common 
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce
RUN export LC_ALL=C
RUN pip install docker-compose
RUN pip install pytest

ENV KUBE_LATEST_VERSION="v1.15.2"
ENV HELM_VERSION="v2.14.3"
ENV DEBIAN_FRONTEND="readline"
ENV RUNLEVEL="1"

RUN wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

RUN apt-get update
RUN apt-get install -y python software-properties-common
RUN apt-add-repository --yes --update ppa:ansible/ansible 
RUN printf "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d 
RUN apt-get -y install ansible ssh python-apt