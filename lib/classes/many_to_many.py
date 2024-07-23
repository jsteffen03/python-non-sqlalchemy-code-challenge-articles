class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    def get_title(self):
        return self._title
    
    def set_title(self, value):
        if type(value) is str and 5 <= len(value) <= 50 and not hasattr(self, "title"):
            self._title = value 
        else: 
            print("No!")
        
    title = property(get_title, set_title)
        
class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 0 < len(value) and not hasattr(self, "name"):
            self._name = value 
        else: 
            print("No!")
        
    name = property(get_name, set_name)

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass