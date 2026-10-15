# 1. Use an official Python base image
FROM python:3.12-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy requirements file (COPY <source> <destination>)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install -r requirements.txt

# 5. Copy all other files
COPY . .

# 6. Document the application port
EXPOSE 5001

# 7. Command to start the application
CMD ["python", "app.py"]