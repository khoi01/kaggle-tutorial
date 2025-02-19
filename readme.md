# Kaggle Learn Environment Setup

This documentation provides a comprehensive guide to setting up a Docker-based environment for Kaggle learning using Jupyter Notebook.

## Prerequisites
Ensure you have the following installed on your system:
- Docker ([Installation Guide](https://docs.docker.com/get-docker/))
- Docker Compose ([Installation Guide](https://docs.docker.com/compose/install/))

## 1. Clone or Create the Project Directory
```bash
mkdir kaggle-learn
cd kaggle-learn
```

## 2. Create a `Dockerfile`
Create a `Dockerfile` with the following content:
```dockerfile
# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Jupyter Notebook
EXPOSE 8888

# Command to start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

## 3. Create a `docker-compose.yml` File
Create a `docker-compose.yml` file with the following content:
```yaml
version: '3.8'

services:
  kaggle-learn:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - .:/app
    container_name: kaggle-learn-container
    command: ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

## 4. Create a `requirements.txt` File
Create a `requirements.txt` file to list the required Python libraries:
```txt
jupyter
pandas
numpy
matplotlib
seaborn
scikit-learn
tensorflow
torch torchvision torchaudio
kaggle
requests
beautifulsoup4
```

## 5. Build and Run the Docker Container
Run the following commands to build and start the container:
```bash
docker-compose build
docker-compose up
```

## 6. Access Jupyter Notebook
Once the container is running, open your browser and go to:
```
http://localhost:8888
```
The terminal will display a URL with a token. Copy and paste it into your browser to access Jupyter Notebook.

## 7. Stopping the Container
To stop the running container, use:
```bash
docker-compose down
```

## 8. Troubleshooting
### Issue: Unable to Pull Docker Image
Try logging into Docker:
```bash
docker login
```
Then pull the Python image manually:
```bash
docker pull python:3.10
```

### Issue: Network Connection Problems in Container
Test internet connectivity inside the container:
```bash
docker run --rm -it python:3.10 bash
ping -c 4 google.com
```
If the connection fails, try changing the DNS settings:
```bash
sudo tee /etc/docker/daemon.json <<EOF
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
EOF
sudo systemctl restart docker
```

### Issue: Slow Package Installation
Use a different PyPI mirror:
```bash
pip install --no-cache-dir -r requirements.txt --index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

---
You now have a fully functional Kaggle learning environment set up in Docker! 🚀
