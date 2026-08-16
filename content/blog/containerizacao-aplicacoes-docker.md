---
title: Containerização de aplicações com Docker
date: 2026-08-16
slug: containerizacao-aplicacoes-docker
description: Uma introdução prática à containerização com Docker, seus principais conceitos, benefícios e o fluxo entre Dockerfile, imagem e container.
tags:
  - MBA   
  - Docker
  - Containers
  - DevOps
  - Arquitetura
---

# Containerização de aplicações com Docker

Executar uma aplicação localmente pode parecer simples até começarem a surgir diferenças de ambiente, dependências, sistema operacional, configurações e versões de software.

Uma aplicação pode envolver, por exemplo:

- banco de dados;
- back-end;
- front-end;
- proxy reverso;
- bibliotecas;
- diferentes versões de runtime.

Quando todos esses componentes dependem diretamente da máquina onde estão instalados, problemas de compartilhamento de recursos, gestão das aplicações, implantação e migração entre ambientes começam a aparecer.

A containerização ajuda a reduzir esse tipo de problema ao empacotar a aplicação junto com os elementos necessários para sua execução em um ambiente isolado e reproduzível.

## O que é Docker?

Docker é uma plataforma para desenvolver, distribuir e executar aplicações utilizando containers.

A proposta é separar a aplicação da infraestrutura onde ela será executada, facilitando a movimentação do software entre diferentes ambientes.

Essa consistência é uma das ideias mais importantes da containerização:

```text
Desenvolvimento
      ↓
Homologação
      ↓
Produção

Mesmo ambiente de execução
```

Em vez de depender de toda a configuração existente na máquina, levamos conosco uma definição do ambiente necessário para executar a aplicação.

## Container não é uma máquina virtual

Containers e máquinas virtuais resolvem alguns problemas semelhantes, mas possuem arquiteturas diferentes.

Em uma máquina virtual, normalmente temos:

```text
Aplicação
Bibliotecas
Sistema Operacional convidado
Hypervisor
Sistema Operacional host
Infraestrutura
```

Já em containers:

```text
Aplicação
Bibliotecas
Container
Docker Engine
Sistema Operacional host
Infraestrutura
```

Containers compartilham a infraestrutura do sistema operacional através do Docker Engine, enquanto máquinas virtuais possuem sistemas operacionais convidados separados.

Isso contribui para containers normalmente terem menos overhead e inicializarem rapidamente.

## Principais benefícios

Entre os principais benefícios da utilização de containers estão:

- isolamento;
- ambientes consistentes;
- portabilidade;
- facilidade de migração;
- uso eficiente de recursos;
- inicialização rápida;
- gestão simplificada;
- integração com práticas DevOps;
- CI/CD;
- atualizações simplificadas;
- possibilidade de rollback.

Um dos pontos mais importantes é a **reprodutibilidade**.

Em vez de documentarmos algo como:

```text
Instale Python.
Instale determinada versão.
Configure as bibliotecas.
Configure as variáveis.
Instale o banco.
Configure o servidor.
```

podemos descrever boa parte desse ambiente como código.

## Dockerfile: a receita da imagem

O `Dockerfile` é um arquivo de texto contendo instruções utilizadas para construir uma imagem Docker.

Entre as instruções mais comuns estão:

```dockerfile
FROM
WORKDIR
COPY
RUN
EXPOSE
CMD
```

Um exemplo simples:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
```

Nesse caso:

```text
FROM
↓
define a imagem base

WORKDIR
↓
define o diretório de trabalho

COPY
↓
leva arquivos para a imagem

RUN
↓
executa comandos durante a construção

EXPOSE
↓
documenta a porta utilizada

CMD
↓
define o processo inicial do container
```

## Dockerfile → Image → Container

Uma maneira simples de entender Docker é separar três conceitos:

```text
Dockerfile
    ↓
  build
    ↓
  Image
    ↓
   run
    ↓
Container
```

### Dockerfile

É a definição de como construir o ambiente.

### Image

É o pacote gerado a partir dessa definição.

Uma imagem contém arquivos, binários, bibliotecas e configurações necessários para executar o container.

As imagens Docker também são construídas em **camadas**. Cada instrução relevante do Dockerfile pode gerar uma nova camada, permitindo reutilização e cache durante novas construções.

### Container

É uma instância em execução da imagem.

Podemos pensar de forma simplificada:

```text
Classe        → objeto
Imagem Docker → container
```

Uma mesma imagem pode gerar vários containers.

## Docker Registry

Depois de construir uma imagem, ela pode ser armazenada em um registry.

O Docker Hub é o registry mais conhecido do ecossistema Docker, mas também existem outros registries públicos e privados.

O fluxo pode ser representado assim:

```text
Dockerfile
     ↓
docker build
     ↓
Imagem local
     ↓
docker push
     ↓
Registry
     ↓
docker pull
     ↓
Outro ambiente
```

## Isolamento de recursos

Um container não é simplesmente uma pasta com arquivos.

O Docker utiliza mecanismos do sistema operacional para criar isolamento entre processos.

Em sistemas Linux, namespaces ajudam a limitar aquilo que um processo dentro do container consegue enxergar, enquanto control groups permitem acompanhar e controlar recursos como CPU e memória.

É importante observar que containers não possuem automaticamente limites rígidos de CPU e memória. Esses limites precisam ser configurados quando necessários.

## Containerização e DevOps

Containerização também possui forte relação com práticas de DevOps.

Uma imagem pode ser construída uma única vez e utilizada ao longo do pipeline:

```text
Código
   ↓
Build
   ↓
Imagem
   ↓
Testes
   ↓
Registry
   ↓
Deploy
```

Isso reduz diferenças entre ambientes e ajuda a tornar o processo de entrega mais previsível.

Por isso, containers aparecem frequentemente associados a ambientes de desenvolvimento reproduzíveis e pipelines de CI/CD.

## Uma forma simples de lembrar

Podemos resumir Docker desta maneira:

```text
Dockerfile
"Como construir?"

        ↓

Image
"O que será executado?"

        ↓

Container
"A aplicação executando"
```

A containerização não elimina todos os problemas de infraestrutura, mas cria uma camada importante de padronização.

O ganho principal não está apenas em "rodar aplicações dentro do Docker".

Está em transformar a configuração do ambiente em algo:

- versionável;
- reproduzível;
- portátil;
- automatizável;
- consistente.

E isso aproxima desenvolvimento, infraestrutura e operação dentro do mesmo ciclo de entrega de software.

## Referências

- Material do MBA: Conteinerização de serviços (Docker)
- Docker Docs — Docker overview: https://docs.docker.com/get-started/docker-overview/
- Docker Docs — Dockerfile: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
- Docker Docs — Images: https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/
- Docker Docs — Resource constraints: https://docs.docker.com/engine/containers/resource_constraints/
