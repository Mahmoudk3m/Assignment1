#base image
FROM python
COPY . /Docker
WORKDIR /Docker
CMD python Assignment1.py
