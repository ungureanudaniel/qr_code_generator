# python version
FROM python:3.10.8

# Set environment variable for disabling the generation of .pyc files, reducing disk usage
ENV PYTHONDONTWRITEBYTECODE 1
# Set environment variable for flushing prints/logs directly to the terminal (or log file) in real-time, rather than waiting in a buffer.
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/qrcodes

# Copy the requirements.txt to the working directory in the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (in case you want to serve the QR code in the future)
EXPOSE 8080
# Set the working directory in the container
WORKDIR /usr/src/qrcodes/app

# Run the Python script when the container launches
CMD ["python", "basic_qrcode.py"]
