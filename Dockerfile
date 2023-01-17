FROM python:3.9.16-alpine3.16
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY myapi.py /app/
CMD [ "python" , "-m" ," uvicorn" , "myapi:app", "--host=0.0.0.0" "--reload"]
