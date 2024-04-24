# Use the official Python image as the base image
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . .

# Install X Server related packages
RUN apt-get update && apt-get install -y \
    libx11-6 \
    libxext-dev \
    libxinerama-dev \
    libxi-dev \
    libxrandr-dev \
    libxcursor-dev \
    libxtst-dev \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
RUN pip install -r requirements.txt

# Command to run the main_app.py script
CMD ["python", "main_app.py"]