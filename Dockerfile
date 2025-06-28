# # Use official Node.js image
# FROM node:24-alpine

# # Set working directory
# WORKDIR /app

# # Copy package.json and lock file
# COPY app/package*.json ./

# # Install dependencies
# RUN npm install

# # Copy the rest of the code
# COPY app/ .

# # Build the Vite app
# RUN npm run build

# # Expose the app port
# EXPOSE 5173

# # Start the app in development mode
# CMD ["npm", "run", "dev", "--", "--host"]

# File: Dockerfile




# File: Dockerfile

FROM python:3.8-slim

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y chromium chromium-driver

# Install Python dependencies
RUN pip install selenium

# Copy test scripts
COPY ./tests /tests

# Set working directory
WORKDIR /tests

# Command to run tests
CMD ["python3", "test_app.py"]
