FROM python:3.11

ENV HOME=/home/app/resume
RUN mkdir -p $HOME
WORKDIR $HOME

COPY requirements.txt .

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY . $HOME

EXPOSE 8000

RUN python3.10 -m pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
