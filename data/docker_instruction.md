# How to ride the camel(Luotuo) with Docker

## 0. Prepare Environment

**Since the Docker Container is built on CUDA 11.8, it is necessary for the CUDA version on your host system to be 11.8 or higher.**

### Install Docker

```bash
curl -fsSL https://get.docker.com | bash -
```

### Install NVIDIA Container Runtime

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

```bash
sudo apt-get update 
sudo apt-get install -y nvidia-container-toolkit
```

```bash
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

## 1. Clone the repo

```bash
git clone https://github.com/LC1332/Luotuo-Chinese-LLM
cd Luotuo-Chinese-LLM
```

## 2. Modify docker-compose.yaml

```yaml
version: "3.9"

services:
  finetune:
    container_name: luotuo
    build: ./docker
```

> To share the host network with the container, please uncomment the following line by removing the "#" symbol.

> Note: By default, a container's network is isolated from the host system, which means that `localhost` or `127.0.0.1` within the container refers to the container itself, **not the host system**.

```
	# network_mode: host
```

> Make the JupyterLab port accessible from the internet. If you have set the network_mode to 'host', disregard this entry.

```
    ports:
      - "8888:8888"
    environment:
```
> Please modify the entries below to configure the IP address and port for JupyterLab to listen on.

``` 
      - JUPYTER_IP=0.0.0.0
      - JUPYTER_PORT=8888
```
> Please modify the entry below to configure the PYPI mirror you wish to use.
```yaml
      - PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple
```
> If you are using a proxy server, please uncomment the entries below and configure accordingly.
```yaml
      # - http_proxy=http://proxy.example.com:port
      # - https_proxy=http://proxy.example.com:port
```
```yaml
    volumes:
      - ./:/workspace
    ulimits:
      memlock:
        soft: -1
        hard: -1
    deploy:
      resources:
        reservations:
          devices:
          - driver: nvidia
            capabilities: [gpu]
```
> Please modify the line below to allocate the desired GPU ID to the container. If you are unsure which ID to use, you can run `nvidia-smi -L` to check.
```yaml
            device_ids: ['0', '1']
```

## 3. Run container and attach into it

```
docker compose build
docker compose up -d
```

After installing the requirements, run `docker compose logs` to retrieve the address and token for Jupyter Lab. You can then open your browser and enter the address to access it.

To access a shell in the container, use the command `docker exec -it luotuo /bin/bash` to start a bash session. Press 'Ctrl + P + Q' to detach from the shell and leave it running in the background, or press 'Ctrl + D' to detach and terminate the session.



Enjoy it! o((>ω< ))o
