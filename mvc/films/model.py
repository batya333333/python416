class Article:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()
