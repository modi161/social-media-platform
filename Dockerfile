FROM python:3.12-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y pkg-config build-essential libmariadb-dev-compat libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Set the environment variable
ENV FLASK_APP=social_media.py

# Expose the port your Flask app runs on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]