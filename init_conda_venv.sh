#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Define default environment name if not specified in environment.yml
DEFAULT_ENV_NAME="my_conda_env"

ENV_NAME=$(grep "name:" "$SCRIPT_DIR/requirements/environment.yml" | cut -d ' ' -f2)


if [ -f "$SCRIPT_DIR/requirements/environment.yml" ]; then
    echo "Found environment.yml. Creating conda environment from it..."

    # Get the environment name from environment.yml, or use the default if not specified
    ENV_NAME=$(grep "name:" "$SCRIPT_DIR/requirements/environment.yml" | cut -d ' ' -f2)

    # If no name found in environment.yml, use default
    if [ -z "$ENV_NAME" ]; then
        ENV_NAME=$DEFAULT_ENV_NAME
    fi

    ENV_PATH="$SCRIPT_DIR/$ENV_NAME"

    # Step 1: Create base environment
    echo "Creating environment: $ENV_PATH using $SCRIPT_DIR/requirements/environment.yml"
    conda env create -p "$ENV_PATH" -f "$SCRIPT_DIR/requirements/environment.yml"


    # Initialize Conda for the current shell if needed
    echo "Initializing Conda for the current shell..."
    eval "$(conda shell.bash hook)"

    # # Step 2: Activate the environment and install pip
    # echo "Activating environment and installing pip..."
    conda activate $ENV_PATH

    pip install -r "$SCRIPT_DIR/requirements/requirements.txt"

    pip install --editable .
    
else
    echo "Error: environment.yml not found in the script's directory!"
    exit 1
fi
# Step 1: Create Mamba base environment
# echo "Creating Mamba environment with Python $PYTHON_VERSION..."
# mamba create -n "$ENV_NAME" python="$PYTHON_VERSION" -y

# # Step 2: Activate the environment and install pip
# echo "Activating environment and installing pip..."
# source activate "$ENV_NAME"
# mamba install pip -y

# # Step 3: Function to install pip packages later
# install_pip_packages() {
#     echo "Installing pip packages..."
#     # Install pip packages passed as arguments to the function
#     pip install "$@"
# }

# # Step 4: Optionally install pip packages passed via command line arguments
# if [ "$#" -gt 0 ]; then
#     install_pip_packages "$@"
# else
#     echo "No pip packages provided at creation. You can install them later using pip."
# fi

# echo "Environment setup complete."
# echo "To activate the environment, run: source activate $ENV_NAME"
