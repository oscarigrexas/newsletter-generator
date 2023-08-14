from dataclasses import dataclass, asdict

from linkpreview import link_preview
from urllib.parse import urlparse


@dataclass
class ArticlePreview:
    title: str
    description: str
    domain: str
    url: str


def generate_article_preview(link: str):
    preview = link_preview(url=link, parser="lxml")
    article_preview = ArticlePreview(
        title=preview.title,
        description=preview.description,
        domain=urlparse(link).netloc,
        url=link,
    )
    return article_preview


def generate_newsletter(links: list[str]):
    previews = [asdict(generate_article_preview(link)) for link in links]
    return previews


def parse_textarea_input(textarea: str):
    links = textarea.split("\n")
    links = [link.strip() for link in links]
    return links
