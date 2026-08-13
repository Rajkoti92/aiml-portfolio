# Use a minimal base image with Python 3.11 installed (matches the backend)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Install dependencies without caching to keep the image small
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Streamlit listens on port 8501
EXPOSE 8501

# Start the Streamlit app, bound to all interfaces so the forwarded port works
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
