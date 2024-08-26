# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# Copy the requirements file to the working directory
COPY requirements.txt ./

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
# Copy the rest of the project files to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Define the command to run the application
CMD ["python3", "-m", "flask", "--app", "app.py", "run"]