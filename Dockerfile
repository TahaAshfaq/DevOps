# Use official Node.js image
FROM node:24-alpine

# Set working directory
WORKDIR /app

# Copy package.json and lock file
COPY app/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY app/ .

# Expose the app port
EXPOSE 5173

# Start the app in development mode
CMD ["npm", "run", "dev", "--", "--host"]



