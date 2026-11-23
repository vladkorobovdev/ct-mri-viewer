# =========================================
# Stage: Development (Angular App)
# =========================================
ARG NODE_VERSION=24-alpine

FROM node:${NODE_VERSION} AS dev

# Set working directory inside the container
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy rest of the source code
COPY . .

# Ensure the "node" user owns the application files
RUN chown -R node:node /app


# Switch to the built-in non-root "node" user
USER node


# Expose Vite dev server port
EXPOSE 4200

# Run Vite in dev mode, accessible outside the container
CMD ["npx", "ng", "serve", "--host", "0.0.0.0"]
