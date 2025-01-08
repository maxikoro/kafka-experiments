# Kafka Experiments

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Создает композитный докер контейнер с кафкой, продюсером и 3мя консюмерами. Контейнер kafka-init после старта кафки создает 2 топика(topic1, topic3), по 3 партиции в каждом. Продюсер генерит белиберду на латыни в topic1. Консюмеры ее читают. Topic3 не используется.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

Вам нужен установленный докер и гит.

### Installing

A step by step series of examples that tell you how to get a development env running.

```
git clone https://github.com/maxikoro/kafka-experiments.git
cd kafka-experiments
docker compose up -d
```

### Если есть проблема с билдом питон контейнеров на хостинге, то вот решение:
The reason for this is issue is an MTU mismatch of your network interfaces. If you open the base image from your Dockerfile in interactive mode: sudo docker run -it {your base image repo} /bin/bash, and run ip a, then do the same on your host OS, you will probably find that they are different. This means that the Docker bridge is dropping packets / failing transmission. If you want bridge networking to work as opposed to host, create a file on your host OS at /etc/docker/daemon.json with the contents
```
{
    "mtu": whatever_your_host_os_MTU_is
}
```
and then run sudo systemctl restart docker, this should probably fix your bridge networking.

## Usage <a name = "usage"></a>

В одном из контейнеров находится web-ui для кафки. Интерфейс доступен по адресу http://localhost:8080. Также в логах докера, как в общих, так и в отдельных, визуально можно понять, что происходит. Можно выключать консюмеров и смотреть, как оставшиеся перехватывают обработку сообщений в топике.
