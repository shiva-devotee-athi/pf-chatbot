FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . ./  # Copy everything in the current directory into the container's /usr/local/app

EXPOSE 8080 # changed to 8080 to match the CMD

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]