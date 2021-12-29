FROM python:3.8.10-alpine

# Install dependencies:
COPY app /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Run the application:
CMD ["python3", "urls.py"]