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
- Git
- GitHub Pages

## Estrutura

```text
.
├── docs/
│   ├── deploy.md
│   ├── design-system.md
│   └── ai-agents.md
├── index.html
├── src/
│   ├── assets/
│   │   └── images/
│   ├── design-system/
│   │   ├── components/
│   │   ├── tokens/
│   │   ├── base.css
│   │   └── styles.css
│   ├── styles/
│   │   └── global.css
│   └── main.js
├── README.md
└── .gitignore
```

## Desenvolvimento

Novas páginas devem manter a estrutura simples e importar:

```html
<link rel="stylesheet" href="./src/styles/global.css">
```

Antes de criar estilos novos, consulte e reutilize o design system em
`src/design-system/`.

## Documentação

- [Design system](docs/design-system.md)
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
