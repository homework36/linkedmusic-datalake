## quick procedures to configure Elasticsearch and Kibana locally

This document contains steps to install and configure Elasticsearch and Kibana on [docker desktop](https://www.docker.com/products/docker-desktop/) (tested on Windows and Mac OS). We do not follow the official documentation and only do minimum configuration for a quick start.

With docker desktop running, do the following steps. Commands should be executed in a terminal.

### 1. Pull docker images for elastic search and kibana.

```bash
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.2
docker pull docker.elastic.co/kibana/kibana:8.10.3
```

### 2. Create a network called *elastic*.

```bash
docker network create elastic
```

### 3. Start an Elasticsearch container called *es01*:

```bash
docker run --rm --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.10.2
```

*The security features are turned off for now for easier data ingestion. Also there is no need to record the password and enrollment token.* Do not close the terminal when the container is running. It usually takes about a minute to initialize.

Go to [http://localhost:9200/](http://localhost:9200/) and verify that you see

```json
{
    "name": "2e657f0b2323",
    "cluster_name": "docker-cluster",
    "cluster_uuid": "0zbLjPwYSH6JIjhGXKB7EA",
    "version": {
        "number": "8.10.2",
        "build_flavor": "default",
        "build_type": "docker",
        "build_hash": "6d20dd8ce62365be9b1aca96427de4622e970e9e",
        "build_date": "2023-09-19T08:16:24.564900370Z",
        "build_snapshot": false,
        "lucene_version": "9.7.0",
        "minimum_wire_compatibility_version": "7.17.0",
        "minimum_index_compatibility_version": "7.0.0"
    },
    "tagline": "You Know, for Search"
}
```

### 4. Start a Kibana container called *kib01*.

```bash
docker run -d -e "xpack.monitoring.enabled=false" -e "xpack.monitoring.ui.container.elasticsearch.enabled=false" --name kib01 --net elastic --restart always -p 5601:5601 docker.elastic.co/kibana/kibana:8.10.3
```

### 5. Connect *kib01* to *es01*.

Run the following command in terminal first:

```bash
docker inspect elastic
```

Get the *IPv4Address* for container *es01*. For example, `172.18.0.2/16`.

Go to [http://localhost:5601/](http://localhost:5601/).

Normally, it will prompt the user to enter an enrollment token. Since the security features are off, there is no way to generate an enrollment token. Therefore, go to **Configure manually** and enter `http://[IPv4Address]:9200`. In the example, http://172.18.0.2/16:9200. Click **Check address** and **Configure Elastic**.

### 6. Enter verification code.

Can see it in the docker container message by clicking *kib01* in docker desktop container page. Enter the 6-digit code on the webpage. Do not use the command line option.

### 7. Wait or refresh the page. Now you are on Kibana.

*There are alternatives such as creating a yml file for Kibana, but this is the easiest way.*
