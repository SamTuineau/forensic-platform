FORENSIC PLATFORM BOOTSTRAP

This document instructs the coding agent to create a complete
cross-platform development environment.

The result must run using:

docker compose up

No business logic is implemented yet.
Only structure and infrastructure.

--------------------------------------------------
SECTION 1 - PROJECT STRUCTURE
--------------------------------------------------

Create directories:

docs
bootstrap
platform
platform/app
platform/app/api
platform/app/core
platform/app/models
platform/app/services
platform/extractors
platform/tests
ui
ui/src
ui/src/components
ui/src/pages
ui/public
infra
infra/docker
infra/scripts
casebundles

--------------------------------------------------
SECTION 2 - SYSTEM SPEC
--------------------------------------------------

Create file docs/SYSTEM_SPEC.md with content:

Forensic Environment Modelling Platform

Mission:
Reconstruct how an unknown server environment works from directory evidence.

Constraints:
Offline capable
Cross platform
Container first
Evidence driven
Modular plugins
Sensitive safe

Modules:
ingestion
extraction
graph construction
inference
sensitivity scanning
api
ui explorer

Storage default is SQLite.
UI runs in browser.

Facts are not inference.

--------------------------------------------------
SECTION 3 - PYTHON BACKEND
--------------------------------------------------

Create file platform/requirements.txt

Content:

fastapi
uvicorn[standard]
pydantic
sqlalchemy
python-multipart
networkx
python-dotenv

--------------------------------------------------

Create file platform/app/main.py

Content:

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Forensic Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Forensic Platform API running"}

--------------------------------------------------
SECTION 4 - API DOCKERFILE
--------------------------------------------------

Create file infra/docker/Dockerfile.api

Content:

FROM python:3.12-slim
WORKDIR /app
COPY platform/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY platform/app ./app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

--------------------------------------------------
SECTION 5 - UI SETUP
--------------------------------------------------

Create file ui/package.json

Content:

{
  "name": "forensic-ui",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.6.0",
    "cytoscape": "^3.26.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "@vitejs/plugin-react": "^4.0.0"
  }
}

--------------------------------------------------

Create file ui/vite.config.js

Content:

import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 5173
  }
})

--------------------------------------------------

Create file ui/index.html

Content:

<!DOCTYPE html>
<html>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

--------------------------------------------------

Create file ui/src/main.jsx

Content:

import React from "react"
import ReactDOM from "react-dom/client"
import App from "./pages/App"

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)

--------------------------------------------------

Create file ui/src/pages/App.jsx

Content:

export default function App() {
  return (
    <div style={{padding:"40px"}}>
      <h1>Forensic Environment Explorer</h1>
      <p>UI running successfully.</p>
    </div>
  )
}

--------------------------------------------------
SECTION 6 - UI DOCKERFILE
--------------------------------------------------

Create file infra/docker/Dockerfile.ui

Content:

FROM node:20
WORKDIR /app
COPY ui/package.json .
RUN npm install
COPY ui .
CMD ["npm","run","dev"]

--------------------------------------------------
SECTION 7 - DOCKER COMPOSE
--------------------------------------------------

Create docker-compose.yml

Content:

version: "3.9"

services:

  api:
    build:
      context: .
      dockerfile: infra/docker/Dockerfile.api
    ports:
      - "8000:8000"
    volumes:
      - ./platform:/app

  ui:
    build:
      context: .
      dockerfile: infra/docker/Dockerfile.ui
    ports:
      - "5173:5173"
    depends_on:
      - api

--------------------------------------------------
SECTION 8 - ENV FILE
--------------------------------------------------

Create .env

APP_ENV=development
API_URL=http://localhost:8000

--------------------------------------------------
SECTION 9 - START SCRIPTS
--------------------------------------------------

Create infra/scripts/start.ps1

docker compose up --build

Create infra/scripts/start.sh

docker compose up --build

--------------------------------------------------
SECTION 10 - GITIGNORE
--------------------------------------------------

Create .gitignore

node_modules
__pycache__
.env
dist
*.db
casebundles

--------------------------------------------------
SUCCESS CRITERIA
--------------------------------------------------

The system must start successfully with:

docker compose up

API available at localhost port 8000
UI available at localhost port 5173