# Site pessoal - Alex Sousa

Site pessoal publicado no GitHub Pages para reunir projetos, estudos,
experimentos e experiências relacionadas a desenvolvimento de software e
tecnologia.

O projeto deve continuar simples: HTML, CSS, JavaScript e arquivos estáticos.

## Conceito

Este site funciona como meu laboratório pessoal de tecnologia.

Ele deve comunicar:

- projetos em desenvolvimento;
- estudos e trilhas de aprendizado;
- experimentos técnicos;
- evolução profissional;
- contato e presença online.

## Tecnologias

- HTML
- CSS
- JavaScript
- Markdown
- Python
- GitHub Actions
- Git
- GitHub Pages

## Estrutura

```text
.
├── .github/
│   └── workflows/
│       └── pages.yml
├── content/
│   └── blog/
├── docs/
│   ├── deploy.md
│   ├── design-system.md
│   └── ai-agents.md
├── scripts/
│   └── build-blog.py
├── src/
│   ├── assets/
│   ├── design-system/
│   ├── styles/
│   │   ├── blog.css
│   │   └── global.css
│   └── main.js
├── templates/
│   └── blog-post.html
├── index.html
├── README.md
└── .gitignore
```

## Blog

O blog usa Markdown como fonte das postagens em `content/blog/`.

Para publicar um novo artigo, crie um arquivo `.md` com front matter:

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

O GitHub Actions executa `scripts/build-blog.py`, gera o site final em `dist/`
e publica o artefato no GitHub Pages. Os HTMLs gerados nao devem ser
versionados.

Na home, o item `Blog` do menu principal direciona para a secao `#blog`.
Dentro dessa secao, o link `Acessar blog` direciona para `./blog/`.

No indice do blog, os links das postagens abrem em nova guia:

- titulo da postagem;
- botao `Ler artigo`.

Links escritos dentro dos artigos Markdown tambem abrem em nova guia no HTML
gerado.

## Desenvolvimento

Novas páginas devem manter a estrutura simples e importar:

```html
<link rel="stylesheet" href="./src/styles/global.css">
```

Antes de criar estilos novos, consulte e reutilize o design system em
`src/design-system/`.

Preview local opcional do site gerado:

```bash
python scripts/build-blog.py
python -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Depois acesse:

```text
http://127.0.0.1:8765/
http://127.0.0.1:8765/blog/
```

## Documentação

- [Design system](docs/design-system.md)
- [Blog](docs/blog.md)
- [Deploy](docs/deploy.md)
- [Agentes de IA](docs/ai-agents.md)

## Agentes de IA

Ao usar agentes de IA para desenvolver novas features, comece pelo arquivo
`AGENTS.md`. Ele contém as instruções operacionais para manter o projeto simples,
seguir o design system e preservar o fluxo de deploy no GitHub Pages.

## Direção técnica

A arquitetura pode evoluir gradualmente conforme novos domínios e
funcionalidades forem adicionados, mas sem adicionar complexidade antes da
necessidade.

Conceitos que podem ser aplicados futuramente:

- Domain-Driven Design (DDD)
- Clean Architecture
- Design Patterns
