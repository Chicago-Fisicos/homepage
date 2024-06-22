# Build the container with this command:
#   docker build -t fisica-pagina-test .

# Run the container with this command:
#   docker run -p 8501:8501 fisica-pagina-test


# Use the official Python image (includes ARM compatibility)
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file first, to leverage Docker cache
COPY requirements.txt /app/

# Install necessary dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . /app/

# Expose port 8501 for Streamlit
EXPOSE 8505

# Healthcheck to verify application health
HEALTHCHECK CMD curl --fail http://localhost:8505/_stcore/health

# Entry point to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "Pages/home.py", "--server.port=8505", "--server.address=0.0.0.0"]
