FROM python:3.11
WORKDIR /coding_challenge_de
COPY ./requirements.txt /coding_challenge_de/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /coding_challenge_de/requirements.txt
RUN pip install fastapi uvicorn
COPY ./app /coding_challenge_de/app
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]