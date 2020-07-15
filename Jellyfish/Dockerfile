FROM python:3

RUN pip3 install --upgrade pip

RUN pip install certifi==2019.6.16
RUN pip install agavepy
RUN pip install chardet==3.0.4
RUN pip install cycler==0.10.0
RUN pip install decorator==4.4.0
RUN pip install idna==2.8
RUN pip install inflection==0.3.1
RUN pip install kiwisolver==1.1.0
RUN pip install marshmallow==2.15.1
RUN pip install matplotlib==3.1.1
RUN pip install networkx==2.3
RUN pip install numpy
RUN pip install pandas==0.25.0
RUN pip install pydent==0.0.35
RUN pip install pyparsing==2.4.2
RUN pip install python-dateutil==2.8.0
RUN pip install pytz==2019.2
RUN pip install requests==2.22.0
RUN pip install six==1.12.0
RUN pip install tqdm==4.23.4
RUN pip install urllib3==1.25.3
RUN pip install xlrd==1.2.0
RUN pip install agavepy

WORKDIR /Jellyfish
COPY . /Jellyfish

RUN export PYTHONPATH=/Jellyfish:$PYTHONPATH
CMD python3 reactor.py ${server} ${file} ${name} ${temp} ${plate}
