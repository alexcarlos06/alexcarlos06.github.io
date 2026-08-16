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

O deploy esperado e via branch principal do repositorio
`alexcarlos06/alexcarlos06.github.io`.

Fluxo comum:

```bash
git status
git add .
git commit -m "feat: adiciona blog estatico com geracao via markdown"
git push origin main
```

O GitHub Actions publica automaticamente a partir da branch `main`, usando o
conteudo gerado em `dist/`.

## Checklist antes do commit

- `git status` nao mostra arquivos inesperados.
- `dist/` permanece como artefato local ignorado pelo Git.
- A pasta `src/design-system/` esta presente.
- Novas paginas usam `src/styles/global.css`.
- Arquivos temporarios, logs e builds nao foram adicionados.
- A pasta original de referencia do design system nao e necessaria para o site
  rodar.

## Observacoes tecnicas

- O projeto usa HTML, CSS, JavaScript puro e Python para geracao estatica do blog.
- Nao adicionar framework sem necessidade clara.
- Python local e opcional e serve apenas para preview/desenvolvimento.
- Regras especificas do blog ficam em `docs/blog.md`.
- Manter a estrutura simples para facilitar manutencao e GitHub Pages.
