![background](https://github.com/baselhusam/damj-platform/blob/main/assets/damj_platform_background.png?raw=true)
# Damj Platform

![Damj_Platform_Demo-ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/9d2e7852-a9f7-4a68-b6cb-2ef386448568)


## Overview

**Damj Platform** is a user-friendly web interface built on top of the Damj Python Package. It provides an intuitive and efficient way to use Damj without needing to manually interact with the Python Package. The Platform simplifies the process, making it **Faster** and **Easier** to perform complex operations by leveraging the power of Streamlit for a sleek and responsive UI. 

Damj Platform was created to bridge the gap between powerful backend tools and end-users who may not be familiar with coding. Whether you are a developer looking to speed up your workflow or someone with limited coding experience, Damj Platform ensures you can utilize the full potential of the Damj Python Package with minimal effort.

## Key Features

- **Intuitive User Interface**: Easily navigate through Damj's features with a clean and simple UI.
- **Streamlined Workflow**: Quickly process and manipulate scripts with just a few clicks.
- **Cross-Platform Compatibility**: Deploy and run on any system with Docker or directly with Python.
- **Fast Setup**: Get started in minutes using Docker, Docker Compose, or by running locally with Python.

## Benefits

- **Ease of Use**: Simplifies complex operations into a few button clicks.
- **Efficiency**: Reduces the time and effort required to perform tasks.
- **Accessibility**: No need to be an expert in Python or Damj to get the most out of the platform.
- **Flexibility**: Works across multiple environments, whether local or containerized.

## How to Deploy
You can use the Damj Service by one of the following ways:

### 1. Cloning and Running Streamlit Normally

To get started by running the Damj Platform locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/baselhusa/damj-platform.git

# Navigate to the project directory
cd damj-platform

# Install the required dependencies
pip install -r requirements.txt

# Run the Streamlit application
streamlit run main.py
```

Open your browser and go to `http://localhost:8501` to start using the platform.

### 2. Running Docker Image

To deploy the platform using Docker:

```bash
# Pull the Docker image from Docker Hub
docker pull baselhusam/damj

# Run the Docker container
docker run --name damj -p 7878:7878 -v </path/to/project>:</mnt/project> baselhusam/damj
```

Access the platform at `http://localhost:7878`.

### 3. Running Docker-Compose File

For an even easier setup, use Docker Compose:

```bash
# Clone the repository
git clone https://github.com/baselhusa/damj-platform.git

# Navigate to the project directory
cd damj-platform

# Run Docker Compose
docker-compose up
```

The platform will be accessible at `http://localhost:7878`.

## How to Use

To use the Damj Platform, simply select the directory of your project, and the platform will automatically load and process the files as per the options you choose. 

Here is a video walkthrough to guide you through the platform's features and show you how to get the most out of it.

https://github.com/user-attachments/assets/7361da26-5920-44f7-87ad-2c9f12908fa9


## Contributors

**Basel Husam**

We welcome contributions from the community. Please feel free to fork the repository, submit issues, or create pull requests!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Other.

- **Documentation**: For detailed documentation on the Damj Python Package, visit the [Damj GitHub Repository](https://github.com/baselhusam/damj).
- **Support**: If you encounter any issues or have any questions, please open an issue in the GitHub repository.
