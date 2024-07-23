class Article:

    all = []

    def __init__(self, author, magazine, title): #inizilation of Article Class
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
            raise ValueError("Not Valid Title")
        
    title = property(get_title, set_title) #properties for title attribute

    def get_magazine(self):
        return self._magazine
    
    def set_magazine(self, value):
        if type(value) is Magazine:
            self._magazine = value
        else:
            raise ValueError("Not Valid Magazine")
    
    magazine = property(get_magazine, set_magazine) #properties for Magazine attribute

    def get_author(self):
        return self._author
    
    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise ValueError("Not Valid Author")
    
    author = property(get_author, set_author) #properties for Author Attribute


class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self) #inizilation of Article Class

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 0 < len(value) and not hasattr(self, "name"):
            self._name = value 
        else: 
            raise ValueError("Not Valid Name")
        
    name = property(get_name, set_name) # properties for name attribute

    def articles(self):# returns list of articles the author has written
        my_articles = []
        for article in Article.all:
            if article.author == self:
                my_articles.append(article)
        return my_articles 

    def magazines(self):#returns the a uniqu list of magazines the author has written for
        my_magazines = []
        
        for article in Article.all:
            if article.author == self and article.magazine not in my_magazines:
                my_magazines.append(article.magazine)
        return my_magazines

    def add_article(self, magazine, title): #inizaltion of the Article Class
        return Article(self, magazine, title)

    def topic_areas(self): #returns a list of categories the author has written under
        my_topics = []

        for article in Article.all:
            if article.author == self and article.magazine.category not in my_topics:
                my_topics.append(article.magazine.category)

        if len(my_topics) == 0 :
            return None
        else:
            return my_topics

class Magazine:

    all = []

    def __init__(self, name, category): #inizialtion of the Magazine Class
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._name = value 
        else: 
            raise ValueError("Not Valid Name")
        
    name = property(get_name, set_name) #properties of name attribute

    def get_category(self):
        return self._category
    
    def set_category(self, value):
        if type(value) is str and 0 < len(value):
            self._category = value 
        else: 
            raise Exception("Not Valid Category")
        
    category = property(get_category, set_category) #properties of Category attribute

    def articles(self): #returns a list of all articles the magazine has puplished
        my_articles = []

        for article in Article.all:
            if article.magazine == self:
                my_articles.append(article)
        return my_articles 


    def contributors(self): #returns a unique list of authors that wrote for magazine
        my_contributors = []
        
        for article in Article.all:
            if article.magazine == self and article.author not in my_contributors:
                my_contributors.append(article.author)
        return my_contributors

    def article_titles(self): #returns a list of all the titles of the articles written for the magazine
        my_titles = []

        for article in Article.all:
            if article.magazine == self:
                my_titles.append(article.title)

        if len(my_titles) == 0:
            return None
        else:
            return my_titles

    def contributing_authors(self): #returns a list of authors who have wrote more than 2 articles for magazine
        author_list = {}
        authors = []


        for article in Article.all:
            if article.magazine == self:
                if article.author in author_list:
                    author_list[article.author] += 1
                else:
                    author_list[article.author] = 1    
        
        for author, count in author_list.items():
            if count > 2:
                authors.append(author)
        
        if len(authors) == 0:
            return None
        else:
            return authors

    @classmethod    
    def top_publisher(self): #returns the top magazine who has puplished the most articles
        publishers_dict = {}
        top_publisher = None
        max_puplishes  = 0

        for article in Article.all:
            if article.magazine == self:
                if publishers_dict.get(article.magazine):
                    publishers_dict[article.magazine] += 1
                else:
                    publishers_dict[article.magazine] = 1
        print(publishers_dict)

        for publisher in publishers_dict:
            if publishers_dict[publisher] > max_puplishes:
                max_puplishes = publishers_dict[publisher]
                top_publisher = publisher
        return top_publisher