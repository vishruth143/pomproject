FROM python:3.9-alpine
RUN mkdir /pomproject/
ADD . /pomproject/
WORKDIR /pomproject/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV GROUP="smoke"
# ENTRYPOINT pytest -s -v -m ${GROUP} --disable-warnings
ENTRYPOINT py.test -s -v --html=reports/report.html --capture=tee-sys --junitxml="reports/result.xml"
