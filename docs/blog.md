# Blog

O blog do site usa Markdown como fonte das postagens, Python como gerador
estatico e GitHub Actions como ambiente oficial de build e publicacao.

## Fluxo

```text
content/blog/*.md -> scripts/build-blog.py -> dist/blog/ -> GitHub Pages
```

Os arquivos Markdown em `content/blog/` sao a fonte oficial do conteudo.
Os HTMLs gerados em `dist/` sao artefatos de build e nao devem ser versionados.

## Como criar uma postagem

Crie um novo arquivo `.md` em `content/blog/` com front matter:

```markdown
---
title: Titulo da postagem
date: 2026-08-16
slug: titulo-da-postagem
description: Resumo curto da postagem.
tags:
  - Arquitetura
  - Python
---

# Titulo da postagem

Conteudo da postagem.
```

Campos obrigatorios:

- `title`
- `date`
- `slug`
- `description`
- `tags`

O `slug` define a URL amigavel:

```text
/blog/titulo-da-postagem/
```

## Navegacao

Na home, o item `Blog` do menu principal deve apontar para a secao `#blog`.
Dentro dessa secao, o link ou botao `Acessar blog` deve apontar para `./blog/`.

Essa decisao preserva a leitura da home antes de levar o visitante para a lista
completa de artigos.

No indice do blog, os links das postagens devem abrir em nova guia:

- titulo da postagem;
- botao `Ler artigo`.

Links escritos dentro dos artigos em Markdown tambem devem abrir em nova guia,
usando `target="_blank"` e `rel="noopener noreferrer"` no HTML gerado.

## Desenvolvimento local

Gere o site:

```bash
python scripts/build-blog.py
```

Sirva o diretorio `dist/`:

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Acesse:

```text
http://127.0.0.1:8765/
http://127.0.0.1:8765/blog/
```

Use a porta `8765` quando `8000` estiver bloqueada no ambiente local.

## Regras para agentes

Quando o usuario solicitar um novo blog ou uma nova postagem:

1. Crie ou edite apenas arquivos Markdown em `content/blog/`, quando a
   infraestrutura do blog ja existir.
2. Nao edite manualmente arquivos em `dist/`.
3. Nao edite manualmente `dist/blog/index.html`.
4. Execute `python scripts/build-blog.py` para validar.
5. Confira se o novo artigo aparece em `/blog/`.
6. Mantenha links de postagens abrindo em nova guia.
7. Preserve o design system existente e o visual escuro com acento verde neon.
