# Deploy

Este site e estatico e foi pensado para publicacao no GitHub Pages.

O deploy oficial e feito pelo GitHub Actions em `.github/workflows/pages.yml`.
O workflow executa o gerador Python, cria o site final em `dist/` e publica esse
diretorio como artefato do GitHub Pages.

Fluxo do blog:

```text
Markdown -> Python -> dist -> GitHub Actions -> GitHub Pages
```

O navegador carrega, a partir do artefato publicado:

- `index.html`
- `blog/index.html`
- `blog/<slug>/index.html`
- `src/styles/global.css`
- `src/styles/blog.css`
- `src/main.js`
- arquivos em `src/assets/`

## Configuracao obrigatoria do GitHub Pages

Como o site final e gerado durante o workflow e publicado a partir de `dist/`,
o GitHub Pages deve usar o proprio GitHub Actions como origem da publicacao.

No repositorio, acesse:

```text
Settings -> Pages -> Build and deployment -> Source
```

A opcao deve estar configurada como:

```text
GitHub Actions
```

Nao use `Deploy from a branch` para este projeto. Nesse modo, o GitHub Pages
publica diretamente os arquivos versionados na branch `main` e ignora o
artefato `dist/` gerado pelo workflow. Como `blog/index.html` e as paginas das
postagens sao criadas apenas dentro de `dist/`, essa configuracao provoca erro
404 em rotas como `/blog/` mesmo quando o workflow de build termina com sucesso.

Para diagnosticar esse problema pela API do GitHub Pages, o campo esperado e:

```text
build_type: workflow
```

Se aparecer `build_type: legacy`, verifique novamente a opcao `Source` em
`Settings -> Pages`.

## Validacao local

Para testar localmente a mesma estrutura publicada pelo GitHub Pages, gere o
artefato e use um servidor estatico.

Com Python:

```bash
python scripts/build-blog.py
python -m http.server 8765 --bind 127.0.0.1 --directory dist
```

Depois acesse:

```text
http://127.0.0.1:8765/
http://127.0.0.1:8765/blog/
```

Use a porta `8765` quando `8000` estiver bloqueada no ambiente local.

Antes de publicar, confira:

- textos em portugues sem erro de encoding;
- links internos funcionando;
- imagem do hero carregando;
- pagina `/blog/` carregando;
- postagens em `/blog/<slug>/` carregando;
- layout desktop;
- layout mobile;
- console do navegador sem erros relevantes.

## Publicacao no GitHub Pages

O deploy esperado e disparado por commits na branch principal do repositorio
`alexcarlos06/alexcarlos06.github.io`.

Fluxo comum:

```bash
git status
git add .
git commit -m "feat: adiciona blog estatico com geracao via markdown"
git push origin main
```

O GitHub Actions executa automaticamente a partir da branch `main`, gera o
conteudo em `dist/`, envia esse diretorio como artefato do GitHub Pages e realiza
o deploy pelo job `deploy`.

O workflow valida a existencia da home, do indice do blog e de pelo menos uma
postagem gerada sem depender de slugs especificos. Assim, adicionar ou remover
artigos Markdown nao exige alterar manualmente a validacao do deploy.

## Checklist antes do commit

- `git status` nao mostra arquivos inesperados.
- `dist/` permanece como artefato local ignorado pelo Git.
- A pasta `src/design-system/` esta presente.
- Novas paginas usam `src/styles/global.css`.
- Arquivos temporarios, logs e builds nao foram adicionados.
- A pasta original de referencia do design system nao e necessaria para o site
  rodar.

## Checklist do deploy

- `Settings -> Pages -> Source` esta configurado como `GitHub Actions`.
- O job `build` do workflow terminou com sucesso.
- A etapa `Validate build output` terminou com sucesso.
- O artefato do Pages foi enviado com sucesso.
- O job `deploy` terminou com sucesso.
- `https://alexcarlos06.github.io/` responde normalmente.
- `https://alexcarlos06.github.io/blog/` responde normalmente.
- Uma rota de postagem em `/blog/<slug>/` responde normalmente.

## Observacoes tecnicas

- O projeto usa HTML, CSS, JavaScript puro e Python para geracao estatica do blog.
- Nao adicionar framework sem necessidade clara.
- Python local e opcional e serve apenas para preview/desenvolvimento.
- Regras especificas do blog ficam em `docs/blog.md`.
- Manter a estrutura simples para facilitar manutencao e GitHub Pages.
