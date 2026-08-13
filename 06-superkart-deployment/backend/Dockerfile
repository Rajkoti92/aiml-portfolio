# Use a minimal base image with Python 3.11 installed
# (the pinned numpy/scikit-learn versions require Python >= 3.10,
#  and the model was serialized under Python 3.11)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . .

# Install dependencies without caching to keep the image small
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Start the API with Gunicorn: 4 workers, bound to port 7860 (the port Hugging Face Spaces expects)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:superkart_sales_api"]
