FROM amazonlinux:2

RUN yum -y groupinstall "Development Tools"
RUN amazon-linux-extras install -y python3.8
RUN yum -y install python3-devel
RUN yum -y install zip unzip

RUN python3 -m pip install --upgrade pip
