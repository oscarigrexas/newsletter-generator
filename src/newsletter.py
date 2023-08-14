from src.article_previews.repository import (
    APIArticlePreviewRepository,
    ModuleArticlePreviewRepository,
)


def generate_newsletter(links: list[str]):
    print(links)
    article_preview_provider = APIArticlePreviewRepository()
    previews = [article_preview_provider.get_preview(link).__dict__ for link in links]
    return previews


def parse_textarea_input(textarea: str):
    links = textarea.split("\n")
    links = [link.strip() for link in links]
    return links
