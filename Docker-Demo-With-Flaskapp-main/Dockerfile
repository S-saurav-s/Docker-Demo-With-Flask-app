# ==============================================================================
# DOCKERFILE FOR COMEDY FLASK APP 🎭
# ==============================================================================
# This file tells Docker how to build a container image for our Flask application
# Think of it as a recipe that Docker follows step by step

# STEP 1: Choose the base image (like choosing an operating system)
# ------------------------------------------------------------------
# FROM specifies what base image to start with
# python:3.8-alpine = Python 3.8 installed on Alpine Linux (a tiny, lightweight Linux)
# Alpine is popular because it's small (~5MB vs ~100MB+ for regular Linux)
# This gives us Python already installed and ready to use
FROM python:3.8-alpine

# STEP 2: Copy our application files into the container
# -----------------------------------------------------
# COPY <source> <destination>
# The dot (.) means "copy everything from current directory on host machine"
# /app is the destination folder inside the container
# This copies: app.py, requirements.txt, Dockerfile, and any other files
COPY . /app

# STEP 3: Set the working directory inside the container
# ------------------------------------------------------
# WORKDIR is like doing "cd /app" in the terminal
# All future commands (RUN, CMD) will be executed from this directory
# If /app doesn't exist, Docker creates it automatically
WORKDIR /app

# STEP 4: Install Python packages
# --------------------------------
# RUN executes commands during the build process (when creating the image)
# These commands run INSIDE the container during build time

# First, upgrade pip (Python package installer) to latest version
# This ensures we have the newest features and bug fixes
RUN pip install --upgrade pip

# Then install all packages listed in requirements.txt
# -r means "read from file"
# This will install Flask and any other dependencies we specified
RUN pip install -r requirements.txt

# STEP 5: Define what command runs when container starts
# -------------------------------------------------------
# CMD specifies the default command that runs when someone starts this container
# Format: CMD ["executable", "parameter1", "parameter2"]
# This is like typing "python app.py" in the terminal
# Only the LAST CMD in a Dockerfile is used (if there are multiple)
CMD ["python", "app.py"]

# ==============================================================================
# HOW TO USE THIS DOCKERFILE:
# ==============================================================================
# 1. Build the image:    docker build -t my-flask-app .
# 2. Run the container:  docker run -p 5000:5000 my-flask-app
# 3. Access the app:     http://localhost:5000
#
# The -p 5000:5000 maps port 5000 from container to port 5000 on your machine
# ==============================================================================