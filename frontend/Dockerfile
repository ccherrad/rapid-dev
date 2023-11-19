# Use node v18.17.0 as the base image
FROM node:18.17.0

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the working directory
COPY . .

# Build the Nuxt application
RUN npm run build

# Expose the port that Nuxt is running on (default is 3000)
EXPOSE 3000

# Start the Nuxt application
CMD ["npm", "run", "dev"]
