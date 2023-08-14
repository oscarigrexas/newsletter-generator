from dataclasses import dataclass, asdict


@dataclass
class ArticlePreview:
    title: str
    description: str
    domain: str
    url: str

