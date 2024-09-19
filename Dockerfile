FROM python:3.12
ADD app.py .
CMD ["python","-u","./app.py"]