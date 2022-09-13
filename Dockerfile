FROM python:3.7
ADD app.py .
RUN pip install -r requirements.txt
CMD ["python","./app.py"]
