class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def get_title(self):
        return self._title
    
    def set_title(self, value):
        if type(value) is str and 5 <= len(value) <= 50 and not hasattr(self, "title"):
            self._title = value 
        else: 
            print("No!")
        
    title = property(get_title, set_title)

    def get_magazine(self):
        return self._magazine
    
    def set_magazine(self, value):
        if type(value) is Magazine:
            self._magazine = value
        else:
            print("No!")
    
    magazine = property(get_magazine, set_magazine)

    def get_author(self):
        return self._author
    
    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            print("No!")
    
    author = property(get_author, set_author)


class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 0 < len(value) and not hasattr(self, "name"):
            self._name = value 
        else: 
            print("No!")
        
    name = property(get_name, set_name)

    def articles(self):
        my_articles = []
        for article in Article.all:
            if article.author == self:
                my_articles.append(article)
            else:
                print("why would you even think that would work bozo")
        return my_articles 

    def magazines(self):
        my_magazines = []
        
        for article in Article.all:
            if article.author == self and article.magazine not in my_magazines:
                my_magazines.append(article.magazine)
            else:
                print("try again buddy")
        return my_magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        my_topics = []

        for article in Article.all:
            if article.author == self and article.magazine.category not in my_topics:
                my_topics.append(article.magazine.category)
            else:
                print("why would you even think that would work bozo")
        if len(my_topics) == 0 :
            return None
        else:
            return my_topics

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._name = value 
        else: 
            print("No!")
        
    name = property(get_name, set_name)

    def get_category(self):
        return self._category
    
    def set_category(self, value):
        if type(value) is str and 0 < len(value):
            self._category = value 
        else: 
            print("No!")
        
    category = property(get_category, set_category)

    def articles(self):
        my_articles = []

        for article in Article.all:
            if article.magazine == self:
                my_articles.append(article)
            else:
                print("why would you even think that would work bozo")
        return my_articles 


    def contributors(self):
        my_contributors = []
        
        for article in Article.all:
            if article.magazine == self and article.author not in my_contributors:
                my_contributors.append(article.author)
            else:
                print("try again buddy")
        return my_contributors

    def article_titles(self):
        my_titles = []

        for article in Article.all:
            if article.magazine == self:
                my_titles.append(article.title)
            else:
                print("why would you even think that would work bozo")
        if len(my_titles) == 0:
            return None
        else:
            return my_titles

    def contributing_authors(self):
        author_list = []
        authors = []

        for article in Article.all:
            if article.magazine == self:
                author_list.append(article.author)   
        
        for author in set(author_list): 
            if author_list.count(author) > 2:
                authors.append(author)
        
        if len(authors) == 0:
            return None
        else:
            return authors

