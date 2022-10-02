FROM python:3.10

# 
WORKDIR /build

# 
COPY ./requirements.txt /build//requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt

# 
COPY ./app /build/app
# COPY . .

RUN ls
WORKDIR /build/app
RUN ls

EXPOSE 8000
# for development
# CMD uvicorn main:app --reload -host 0.0.0.0 --port 80
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


EXPOSE 8000
EXPOSE 80