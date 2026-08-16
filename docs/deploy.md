# Deploy

Este site é estático e foi pensado para publicação no GitHub Pages.

Não há etapa de build obrigatória. O navegador carrega diretamente:

- `index.html`
- `src/styles/global.css`
- `src/main.js`
- arquivos em `src/assets/`

## Validação local

Para testar localmente, abra `index.html` no navegador ou use um servidor
estático.

Com Python:

```bash
python -m http.server 8087 --bind 127.0.0.1
```

Depois acesse:

```text
http://127.0.0.1:8087/index.html
```

Antes de publicar, confira:

- textos em português sem erro de encoding;
- links internos funcionando;
- imagem do hero carregando;
- layout desktop;
- layout mobile;
- console do navegador sem erros relevantes.

## Publicação no GitHub Pages

O deploy esperado é via branch principal do repositório
`alexcarlos06/alexcarlos06.github.io`.

Fluxo comum:

```bash
git status
git add .
git commit -m "Atualiza site pessoal"
git push origin main
```

O GitHub Pages deve publicar automaticamente a partir da branch `main`, usando
o arquivo `index.html` na raiz.

## Checklist antes do commit

- `git status` não mostra arquivos inesperados.
- A pasta `src/design-system/` está presente.
- Novas páginas usam `src/styles/global.css`.
- Arquivos temporários, logs e builds não foram adicionados.
- A pasta original de referência do design system não é necessária para o site
  rodar.

## Observações técnicas

- O projeto usa HTML, CSS e JavaScript puros.
- Não adicionar framework sem necessidade clara.
- Não criar etapa de build enquanto o site puder continuar estático.
- Manter a estrutura simples para facilitar manutenção e GitHub Pages.
