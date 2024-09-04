FROM python:3.9-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    xclip

RUN git clone https://github.com/baselhusam/damj-platform.git .

RUN pip3 install -r requirements.txt

EXPOSE 7878

HEALTHCHECK CMD curl --fail http://localhost:7878/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=7878", "--server.address=0.0.0.0"]
