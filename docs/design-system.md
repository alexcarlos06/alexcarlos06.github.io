# Design system

Este projeto usa um design system simples em CSS puro, localizado em
`src/design-system/`.

Novas páginas devem importar sempre:

```html
<link rel="stylesheet" href="./src/styles/global.css">
```

`src/styles/global.css` importa `src/design-system/styles.css` e adiciona
ajustes específicos do site.

O blog também importa `src/styles/blog.css` para estilos específicos de lista
de artigos e leitura de postagens. Esse arquivo deve continuar dependente dos
tokens e componentes existentes.

## Conceito visual

O site é um laboratório pessoal de tecnologia. A identidade visual deve manter:

- fundo quase preto com leve matiz verde;
- acento principal verde neon;
- uso pontual de âmbar para estudos, como MBA e trilhas de aprendizado;
- cantos retos em botões, cards, inputs e blocos;
- Inter para texto e títulos;
- JetBrains Mono para navegação, botões, tags, labels e detalhes técnicos;
- layout limpo, direto e sem excesso de decoração.

Evite gradientes decorativos, elementos muito arredondados, excesso de cards e
efeitos de escala no hover.

## Estrutura

```text
src/design-system/
├── styles.css
├── base.css
├── tokens/
│   ├── colors.css
│   ├── fonts.css
│   ├── spacing.css
│   └── typography.css
└── components/
    ├── buttons.css
    ├── cards.css
    ├── code.css
    ├── forms.css
    ├── nav.css
    └── table.css
```

## Componentes principais

Use os componentes existentes antes de criar novos estilos.

Botões:

- `.btn`
- `.btn-primary`
- `.btn-secondary`
- `.btn-ghost`
- `.btn-icon`

Cards:

- `.card`
- `.card-title`
- `.card-body`
- `.card-kicker`
- `.card-meta`

Tags:

- `.tag`
- `.tag-accent`
- `.tag-accent-2`
- `.tag-neutral`
- `.tag-outline`

Navegação:

- `.nav`
- `.nav-content`
- `.nav-brand`
- `.nav-links`

Outros:

- `.input`
- `.table`
- `.code-block`
- `code.inline`

## Regras para novas páginas

1. Mantenha HTML, CSS e JavaScript simples.
2. Reutilize `src/styles/global.css`.
3. Reutilize tokens de cor, tipografia e espaçamento.
4. Crie CSS novo apenas quando o componente existente não resolver.
5. Mantenha português do Brasil nos textos.
6. Use labels curtas e diretas.
7. Use números de seção quando fizer sentido: `01`, `02`, `03`.
8. Use verde neon para ações principais.
9. Use âmbar apenas para estudos, MBA, cursos e trilhas.
10. Não use emojis na interface.

## Tom de conteúdo

O tom é pessoal, técnico e direto. O site deve parecer um espaço próprio de
estudo, construção e registro de projetos, não uma landing page genérica.

Prefira frases como:

- "Meu laboratório pessoal de tecnologia."
- "Projetos, estudos e experimentos."
- "Trilhas técnicas."
- "Acompanhamento de módulos, resumos e aplicações práticas."

Evite textos publicitários, promessas exageradas e jargão sem necessidade.
