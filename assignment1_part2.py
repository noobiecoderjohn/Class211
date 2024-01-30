class Book:

        def __init__(self, author="", title=""):
                self.author = author
                self.title = title
            
        def display(self):
                print(f"'{self.title}' by {self.author}'")
        
object1 = Book("Happy Potter and the Goblet of Fire", "J. K. Rowling")
object1.display()
object2 = Book("Ivanhoe: A Romance", "Walter Scott")
object2.display()