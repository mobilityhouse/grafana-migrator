FROM python:3.6.1

COPY /src /bench
WORKDIR /bench
RUN pip install -r requirements.txt

CMD /bin/bash
