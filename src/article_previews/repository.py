import os

import requests
from linkpreview import link_preview
from urllib.parse import urlparse

from src.article_previews.model import ArticlePreview


class AbstractArticlePreviewRepository:
    def get_preview(link: str) -> ArticlePreview:
        raise NotImplementedError


class ModuleArticlePreviewRepository(AbstractArticlePreviewRepository):
    def get_preview(self, link: str):
        preview = link_preview(url=link, parser="lxml")
        article_preview = ArticlePreview(
            title=preview.title,
            description=preview.description,
            domain=urlparse(link).netloc,
            url=link,
        )
        return article_preview


class APIArticlePreviewRepository(AbstractArticlePreviewRepository):
    def get_preview(self, link: str):
        API_KEY = os.environ.get("LINKPREVIEW_API_KEY")
        r = requests.get(
            url="http://api.linkpreview.net/",
            params={
                "key": API_KEY,
                "q": link,
            },
        )
        preview = r.json()
        article_preview = ArticlePreview(
            title=preview["title"],
            description=preview["description"],
            domain=urlparse(link).netloc,
            url=link,
        )
        return article_preview
