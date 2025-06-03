# Stage 1: Build the React app
#  as builder
FROM node:18-alpine

WORKDIR /app

COPY package*.json .

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Set the API URL build argument (can be overridden at build time)
ARG REACT_APP_API_URL=http://localhost:8002/api
ENV REACT_APP_API_URL=${REACT_APP_API_URL}

EXPOSE 5173
CMD ["npm", "run", "dev"]

# Build the React app for production
# RUN npm run build

# Stage 2: Serve the static files with Nginx
# Use a recent stable version
# FROM nginx:1.25-alpine

# Remove default Nginx configuration
# RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration (see nginx.conf below)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built static files from the 'builder' stage
# COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80 (Nginx default)
# EXPOSE 80

# Start Nginx
# CMD ["nginx", "-g", "daemon off;"]