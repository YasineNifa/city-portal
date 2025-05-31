# frontend/Dockerfile

# Stage 1: Build the React app
FROM node:18-alpine as builder

WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json .
# COPY yarn.lock ./ # If using yarn

# Install dependencies
RUN npm install
# RUN yarn install # If using yarn

# Copy the rest of the application code
COPY . .

# Set the API URL build argument (can be overridden at build time)
ARG REACT_APP_API_URL=http://localhost:8002/api
ENV REACT_APP_API_URL=${REACT_APP_API_URL}

# Build the React app for production
RUN npm run build
# RUN yarn build # If using yarn

# Stage 2: Serve the static files with Nginx
# Use a recent stable version
FROM nginx:1.25-alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration (see nginx.conf below)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built static files from the 'builder' stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 (Nginx default)
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]