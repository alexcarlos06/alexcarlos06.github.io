# Instruções para agentes de IA

Este repositório é o site pessoal de Alex Sousa, publicado no GitHub Pages.

Antes de alterar qualquer arquivo, leia:

1. `README.md`
2. `docs/design-system.md`
3. `docs/deploy.md`

## Objetivo do projeto

O site é um laboratório pessoal de tecnologia para reunir:

- projetos;
- estudos;
- trilhas de aprendizado;
- experimentos técnicos;
- evolução profissional;
- contato e presença online.

## Regras principais

- Mantenha a estrutura simples.
- Use HTML, CSS e JavaScript puros.
- Não adicione framework, bundler, dependência ou etapa de build sem necessidade explícita.
- Novas páginas devem importar `src/styles/global.css`.
- Reutilize o design system em `src/design-system/`.
- Crie CSS novo apenas quando os componentes existentes não resolverem.
- Preserve o visual escuro, verde neon como acento principal e âmbar apenas para estudos.
- Mantenha os textos em português do Brasil.
- Não use emojis na interface.

## Arquivos importantes

- `index.html`: página inicial.
- `src/styles/global.css`: estilos globais do site e ajustes específicos.
- `src/design-system/`: tokens, base e componentes reutilizáveis.
- `src/main.js`: JavaScript simples da página.
- `docs/design-system.md`: regras visuais e componentes.
- `docs/deploy.md`: validação local e deploy.

## Fluxo recomendado para novas features

1. Entenda a feature solicitada.
2. Verifique se ela é uma nova seção, nova página ou ajuste visual.
3. Reutilize classes existentes como `.btn`, `.card`, `.tag`, `.nav`.
4. Se precisar de CSS novo, coloque no arquivo mais específico possível.
5. Valide visualmente em desktop e mobile.
6. Verifique se os links e imagens funcionam.
7. Confira `git status` antes de finalizar.
8. Ao final de cada interação, pergunte ao usuário se algum aprendizado,
   decisão ou padrão novo deve ser registrado na documentação.

## Aprendizado contínuo

Depois de concluir uma tarefa, o agente deve perguntar explicitamente:

```text
Deseja que eu atualize a documentação com algum aprendizado desta interação?
```

Se o usuário confirmar, registre a informação no arquivo adequado:

- `README.md` para contexto geral do projeto;
- `docs/design-system.md` para decisões visuais e componentes;
- `docs/deploy.md` para validação, publicação e fluxo técnico;
- `docs/ai-agents.md` ou `AGENTS.md` para regras de atuação de agentes.

Não atualize a documentação automaticamente sem confirmação quando a mudança
for apenas uma preferência pontual ou uma decisão ainda não consolidada.

## Deploy

O deploy é feito pelo GitHub Pages a partir da branch `main`.

Não há build obrigatório. O arquivo `index.html` fica na raiz.

Para testar localmente:

```bash
python -m http.server 8087 --bind 127.0.0.1
```

Depois acesse:

```text
http://127.0.0.1:8087/index.html
```

## Cuidados

- Não remova `src/design-system/`.
- Não altere a identidade visual sem pedido explícito.
- Não transforme o projeto em SPA ou aplicação com framework sem aprovação.
- Não adicione arquivos temporários, logs ou builds ao Git.
