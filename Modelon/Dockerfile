# Use the official Python image as the base image
FROM python:3.12.2

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project directory into the container
COPY . .

# Install pytest and any other dependencies
RUN pip install -r requirements.txt

# Command to run the main_app.py script
CMD ["python", "main_app.py"]
