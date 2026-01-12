class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(author, Author):
            raise Exception("Author must be Author instance")

        
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be Magazine instance")

        
        if not isinstance(title, str):
            raise Exception("Title must be string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title length must be 5-50 chars")

        self._title = title  
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        
        if not isinstance(name, str):
            raise Exception("Name must be string")
        if len(name) == 0:
            raise Exception("Name must be > 0 length")

        self._name = name 

    @property
    def name(self):
        return self._name

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be Magazine instance")
        return Article(self, magazine, title)

    def topic_areas(self):
        arts = self.articles()
        if not arts:
            return None
        return list({a.magazine.category for a in arts})


class Magazine:
    def __init__(self, name, category):
        
        if not isinstance(name, str):
            raise Exception("Magazine name must be string")
        if not (2 <= len(name) <= 16):
            raise Exception("Magazine name length must be 2-16 chars")

        
        if not isinstance(category, str):
            raise Exception("Magazine category must be string")
        if len(category) == 0:
            raise Exception("Magazine category must be > 0 length")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be string")
        if not (2 <= len(value) <= 16):
            raise Exception("Magazine name length must be 2-16 chars")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine category must be string")
        if len(value) == 0:
            raise Exception("Magazine category must be > 0 length")
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if len(arts) == 0:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        contribs = {}
        for a in self.articles():
            contribs[a.author] = contribs.get(a.author, 0) + 1

        result = [author for author, count in contribs.items() if count > 2]

        return result if result else None
