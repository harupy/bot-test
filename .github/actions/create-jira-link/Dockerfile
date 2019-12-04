FROM python:3

RUN pip install PyGithub

ADD entrypoint.sh /entrypoint.sh
ADD main.py /main.py
RUN chmod +x /entrypoint.sh
ENTRYPOINT python /main.py