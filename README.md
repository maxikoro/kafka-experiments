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
docker-compose up -d
```

## Usage <a name = "usage"></a>

В одном из контейнеров находится web-ui для кафки. Интерфейс доступен по адресу http://localhost:8080. Также в логах докера, как в общих, так и в отдельных, визуально можно понять, что происходит. Можно выключать консюмеров и смотреть, как оставшиеся перехватывают обработку сообщений в топике.
