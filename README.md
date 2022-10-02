# sentiment-recognition
Sample sentiment recognition app built in order to try out FastAPI.

## Installation

Use docker to run the application.
Build the image with:

```bash
docker build -t sentiment .
```

Run the container with:
```bash
docker run --name sentiment-recognition --expose 80 -p 80:80 sentiment
```
