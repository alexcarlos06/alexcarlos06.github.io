from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "blog"
DIST_DIR = ROOT / "dist"
TEMPLATE_PATH = ROOT / "templates" / "blog-post.html"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Post:
    title: str
    date: date
    slug: str
    description: str
    tags: list[str]
    html_content: str
    source_path: Path

    @property
    def formatted_date(self) -> str:
        return self.date.strftime("%d/%m/%Y")


def main() -> None:
    posts = load_posts()
    prepare_dist()
    copy_static_site()
    build_blog_index(posts)
    build_posts(posts)
    print(f"Build concluido: {len(posts)} postagem(ns) gerada(s) em {DIST_DIR}")


def load_posts() -> list[Post]:
    if not CONTENT_DIR.exists():
        return []

    posts = [parse_post(path) for path in sorted(CONTENT_DIR.glob("*.md"))]
    slugs = [post.slug for post in posts]
    duplicated = sorted({slug for slug in slugs if slugs.count(slug) > 1})
    if duplicated:
        raise ValueError(f"Slug duplicado em postagens: {', '.join(duplicated)}")

    return sorted(posts, key=lambda post: post.date, reverse=True)


def parse_post(path: Path) -> Post:
    raw = path.read_text(encoding="utf-8")
    metadata, markdown = split_front_matter(raw, path)
    validate_metadata(metadata, path)

    return Post(
        title=metadata["title"],
        date=datetime.strptime(metadata["date"], "%Y-%m-%d").date(),
        slug=metadata["slug"],
        description=metadata["description"],
        tags=metadata["tags"],
        html_content=markdown_to_html(markdown),
        source_path=path,
    )


def split_front_matter(raw: str, path: Path) -> tuple[dict[str, object], str]:
    if not raw.startswith("---\n"):
        raise ValueError(f"{path}: front matter YAML ausente")

    try:
        _, front_matter, markdown = raw.split("---\n", 2)
    except ValueError as exc:
        raise ValueError(f"{path}: front matter YAML incompleto") from exc

    return parse_front_matter(front_matter, path), markdown.strip()


def parse_front_matter(front_matter: str, path: Path) -> dict[str, object]:
    metadata: dict[str, object] = {}
    current_list: str | None = None

    for line in front_matter.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("- "):
            if current_list is None:
                    raise ValueError(f"{path}: item de lista sem campo associado")
            metadata[current_list].append(stripped[2:].strip())
            continue

        if ":" not in line:
            raise ValueError(f"{path}: linha invalida no front matter: {line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_list = None

        if value:
            metadata[key] = value.strip('"').strip("'")
        else:
            metadata[key] = []
            current_list = key

    return metadata


def validate_metadata(metadata: dict[str, object], path: Path) -> None:
    required = ["title", "date", "slug", "description", "tags"]
    missing = [field for field in required if field not in metadata]
    if missing:
        raise ValueError(f"{path}: campos obrigatórios ausentes: {', '.join(missing)}")

    for field in ["title", "date", "slug", "description"]:
        if not isinstance(metadata[field], str) or not metadata[field].strip():
            raise ValueError(f"{path}: campo '{field}' deve ser texto não vazio")

    try:
        datetime.strptime(metadata["date"], "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(f"{path}: campo 'date' deve usar o formato YYYY-MM-DD") from exc

    if not SLUG_RE.match(str(metadata["slug"])):
        raise ValueError(f"{path}: campo 'slug' deve usar apenas letras minusculas, numeros e hifens")

    if not isinstance(metadata["tags"], list) or not metadata["tags"]:
        raise ValueError(f"{path}: campo 'tags' deve conter ao menos uma tag")


def prepare_dist() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()


def copy_static_site() -> None:
    for item in ROOT.iterdir():
        if item.name in {".git", ".github", "content", "dist", "docs", "scripts", "templates"}:
            continue
        if item.name.startswith(".") and item.name not in {".nojekyll"}:
            continue

        target = DIST_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)

    cname = ROOT / "CNAME"
    if cname.exists():
        shutil.copy2(cname, DIST_DIR / "CNAME")

    (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")


def build_blog_index(posts: list[Post]) -> None:
    cards = "\n".join(render_post_card(post) for post in posts)
    if not cards:
        cards = '<p class="section__text">Nenhuma postagem publicada ainda.</p>'
    tag_options = render_tag_options(posts)
    date_options = render_date_options(posts)

    html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Artigos de Alex Sousa sobre arquitetura de software, estudos, tecnologia e aprendizados praticos.">

    <title>Blog | Alex Sousa</title>

    <link rel="stylesheet" href="../src/styles/global.css">
    <link rel="stylesheet" href="../src/styles/blog.css">
</head>

<body>
    <header class="nav">
        <div class="container nav-content">
            <a href="../index.html" class="nav-brand">Alex Sousa</a>

            <nav class="nav-links" aria-label="Navegacao principal">
                <a href="../index.html#sobre">Sobre</a>
                <a href="../index.html#projetos">Projetos</a>
                <a href="./">Blog</a>
                <a href="../index.html#estudos">Estudos</a>
                <a href="../index.html#stack">Stack</a>
                <a href="../index.html#contato">Contato</a>
            </nav>
        </div>
    </header>

    <main class="blog-page">
        <section class="container blog-list">
            <header class="blog-list__header">
                <span class="card-kicker">Blog</span>
                <h1 class="blog-list__title">Artigos</h1>
                <p class="blog-list__description">
                    Anotações sobre arquitetura, ferramentas, programação e aprendizados práticos do dia a dia.
                </p>
            </header>

            <form class="blog-filters" aria-label="Filtros de postagens">
                <div class="field blog-filters__field">
                    <label for="filter-tag">Tag</label>
                    <select class="input" id="filter-tag" name="tag">
                        <option value="">Todas</option>
                        {tag_options}
                    </select>
                </div>

                <div class="field blog-filters__field">
                    <label for="filter-date">Publicação</label>
                    <select class="input" id="filter-date" name="date">
                        <option value="">Todas</option>
                        {date_options}
                    </select>
                </div>

                <button class="btn btn-secondary blog-filters__clear" type="button" data-clear-filters>
                    Limpar
                </button>
            </form>

            <p class="blog-filter-status" data-filter-status aria-live="polite"></p>

            <div class="blog-list__grid">
                {cards}
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            © <span id="current-year"></span> Alex Sousa.
        </div>
    </footer>

    <script src="../src/main.js"></script>
    <script>
        const blogPosts = Array.from(document.querySelectorAll("[data-blog-post]"));
        const tagFilter = document.querySelector("#filter-tag");
        const dateFilter = document.querySelector("#filter-date");
        const clearFilters = document.querySelector("[data-clear-filters]");
        const filterStatus = document.querySelector("[data-filter-status]");

        function optionExists(select, value) {{
            return !value || Array.from(select.options).some((option) => option.value === value);
        }}

        function applyInitialFilters() {{
            const params = new URLSearchParams(window.location.search);
            const tag = params.get("tag") || "";
            const date = params.get("date") || "";

            if (optionExists(tagFilter, tag)) {{
                tagFilter.value = tag;
            }}

            if (optionExists(dateFilter, date)) {{
                dateFilter.value = date;
            }}
        }}

        function syncFilterUrl() {{
            const params = new URLSearchParams();

            if (tagFilter.value) {{
                params.set("tag", tagFilter.value);
            }}

            if (dateFilter.value) {{
                params.set("date", dateFilter.value);
            }}

            const query = params.toString();
            const nextUrl = query ? `${{window.location.pathname}}?${{query}}` : window.location.pathname;
            window.history.replaceState(null, "", nextUrl);
        }}

        function updateBlogFilters(syncUrl = true) {{
            const selectedTag = tagFilter.value;
            const selectedDate = dateFilter.value;
            let visibleCount = 0;

            blogPosts.forEach((post) => {{
                const tags = post.dataset.tags.split("|");
                const date = post.dataset.date;
                const matchesTag = !selectedTag || tags.includes(selectedTag);
                const matchesDate = !selectedDate || date === selectedDate;
                const shouldShow = matchesTag && matchesDate;

                post.hidden = !shouldShow;
                if (shouldShow) {{
                    visibleCount += 1;
                }}
            }});

            filterStatus.textContent = visibleCount === 1
                ? "1 postagem encontrada."
                : `${{visibleCount}} postagens encontradas.`;

            if (syncUrl) {{
                syncFilterUrl();
            }}
        }}

        tagFilter.addEventListener("change", updateBlogFilters);
        dateFilter.addEventListener("change", updateBlogFilters);
        clearFilters.addEventListener("click", () => {{
            tagFilter.value = "";
            dateFilter.value = "";
            updateBlogFilters();
        }});
        applyInitialFilters();
        updateBlogFilters(false);
    </script>
</body>
</html>
"""
    blog_dir = DIST_DIR / "blog"
    blog_dir.mkdir(parents=True, exist_ok=True)
    (blog_dir / "index.html").write_text(html_doc, encoding="utf-8")


def build_posts(posts: list[Post]) -> None:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    for post in posts:
        post_dir = DIST_DIR / "blog" / post.slug
        post_dir.mkdir(parents=True, exist_ok=True)
        rendered = render_template(
            template,
            {
                "asset_prefix": "../../",
                "title": html.escape(post.title),
                "description": html.escape(post.description),
                "formatted_date": post.formatted_date,
                "tags_html": render_tags(post.tags),
                "content": post.html_content,
            },
        )
        (post_dir / "index.html").write_text(rendered, encoding="utf-8")


def render_post_card(post: Post) -> str:
    tags_data = html.escape("|".join(post.tags), quote=True)
    return f"""<article class="card elev-sm post-card" data-blog-post data-tags="{tags_data}" data-date="{post.date.isoformat()}">
    <header class="post-card__header">
        <span class="card-meta">{post.formatted_date}</span>
        <h2 class="post-card__title">
            <a href="./{html.escape(post.slug)}/">{html.escape(post.title)}</a>
        </h2>
    </header>
    <p class="post-card__description">{html.escape(post.description)}</p>
    <div class="post-card__tags">
        {render_tags(post.tags)}
    </div>
    <a class="btn btn-secondary" href="./{html.escape(post.slug)}/">Ler artigo</a>
</article>"""


def render_tag_options(posts: list[Post]) -> str:
    tags = sorted({tag for post in posts for tag in post.tags}, key=str.casefold)
    return "\n".join(f'<option value="{html.escape(tag, quote=True)}">{html.escape(tag)}</option>' for tag in tags)


def render_date_options(posts: list[Post]) -> str:
    dates = sorted({post.date for post in posts}, reverse=True)
    return "\n".join(
        f'<option value="{item.isoformat()}">{item.strftime("%d/%m/%Y")}</option>' for item in dates
    )


def render_tags(tags: list[str]) -> str:
    return "\n".join(f'<span class="tag tag-outline">{html.escape(tag)}</span>' for tag in tags)


def render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{ " + key + " }}", value)
    return rendered


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    html_lines: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    in_code = False
    code_lang = ""
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            html_lines.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            html_lines.append("<ul>")
            html_lines.extend(f"<li>{item}</li>" for item in list_items)
            html_lines.append("</ul>")
            list_items.clear()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                language_class = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                code = html.escape("\n".join(code_lines))
                html_lines.append(f"<pre><code{language_class}>{code}</code></pre>")
                in_code = False
                code_lang = ""
                code_lines.clear()
            else:
                flush_paragraph()
                flush_list()
                in_code = True
                code_lang = stripped[3:].strip()
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            html_lines.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue

        if stripped.startswith("> "):
            flush_paragraph()
            flush_list()
            html_lines.append(f"<blockquote>{inline_markdown(stripped[2:])}</blockquote>")
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            list_items.append(inline_markdown(stripped[2:]))
            continue

        paragraph.append(stripped)

    if in_code:
        raise ValueError("Bloco de codigo Markdown nao foi fechado")

    flush_paragraph()
    flush_list()
    return "\n".join(html_lines)


def inline_markdown(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    rendered_parts: list[str] = []

    for part in parts:
        if part.startswith("`") and part.endswith("`"):
            rendered_parts.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue

        escaped = html.escape(part)
        escaped = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", render_image, escaped)
        escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", render_link, escaped)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
        escaped = auto_link_urls(escaped)
        rendered_parts.append(escaped)

    return "".join(rendered_parts)


def render_link(match: re.Match[str]) -> str:
    label = match.group(1)
    url = html.escape(match.group(2), quote=True)
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'


def auto_link_urls(text: str) -> str:
    html_parts = re.split(r"(<a\b[^>]*>.*?</a>|<img\b[^>]*>)", text)
    return "".join(part if part.startswith("<") else link_plain_urls(part) for part in html_parts)


def link_plain_urls(text: str) -> str:
    return re.sub(r"https?://[^\s<]+", render_plain_url, text)


def render_plain_url(match: re.Match[str]) -> str:
    url = match.group(0).rstrip(".,;:")
    suffix = match.group(0)[len(url):]
    escaped_url = html.escape(url, quote=True)
    return f'<a href="{escaped_url}" target="_blank" rel="noopener noreferrer">{url}</a>{suffix}'


def render_image(match: re.Match[str]) -> str:
    alt = match.group(1)
    url = html.escape(match.group(2), quote=True)
    return f'<img src="{url}" alt="{alt}">'


if __name__ == "__main__":
    main()
