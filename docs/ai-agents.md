# Agentes de IA

Este arquivo orienta agentes de IA que forem usados para desenvolver novas
features neste repositório, inclusive quando o projeto for aberto pelo celular.

## Leitura inicial obrigatória

Antes de implementar qualquer mudança, leia:

- `README.md`
- `docs/design-system.md`
- `docs/deploy.md`
- `AGENTS.md`

## Resumo rápido

Este é um site pessoal estático de Alex Sousa, publicado no GitHub Pages.

O projeto deve continuar simples:

- HTML;
- CSS;
- JavaScript;
- sem framework;
- sem build obrigatório.

## Como desenvolver

Para novas seções ou páginas:

1. Use `src/styles/global.css`.
2. Reutilize `src/design-system/`.
3. Prefira componentes existentes antes de criar novos.
4. Mantenha português do Brasil.
5. Valide desktop e mobile.
6. Mantenha o deploy compatível com GitHub Pages.
7. Ao final da interação, pergunte se algum aprendizado deve ser registrado na documentação.

## Aprendizado contínuo

Após cada interação, o agente deve perguntar ao usuário:

```text
Deseja que eu atualize a documentação com algum aprendizado desta interação?
```

Use a resposta do usuário para decidir se a documentação deve ser atualizada.

Quando houver atualização:

- use `README.md` para contexto geral;
- use `docs/design-system.md` para decisões visuais;
- use `docs/deploy.md` para fluxo de publicação e validação;
- use `docs/ai-agents.md` ou `AGENTS.md` para regras de atuação de agentes.

## O que evitar

- Criar estrutura complexa sem necessidade.
- Adicionar React, Vite, Next.js ou outro framework sem pedido explícito.
- Criar etapa de build obrigatória.
- Ignorar o design system.
- Substituir o visual do site por outro estilo.
- Usar emojis na interface.

## Referência principal

Se houver conflito entre preferência estética e simplicidade técnica, priorize:

1. manter o projeto simples;
2. preservar o design system;
3. entregar a feature solicitada com menor mudança possível;
4. manter o site publicável no GitHub Pages.
