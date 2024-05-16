# Create a postgress database tables ==3
# Authors: id, first_NAME, last_name
# books: id, title, and number of pages columns
# AuthorBooks: id, author id, book id

# we separate author book pairings so we can easily store multiple books by the same author
# For books with multiple authors, multiple entries would be added to the AuthorBooks table

# The books table should be updated with the new book.
# if the author is a new author, then authors should be updated to include the new author
# The AuthorBooks table should be updated as well


from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import registry, Session, relationship

engine=create_engine('postgresql://postgres:password@localhost:5433/library')

mapper_registry = registry()
Base = mapper_registry.generate_base()

class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    def __repr__(self):
        return "<Author(author_id='{0}', first_name = '{1}', last_name='{2}')>".format(self.author_id, self.first_name, self.last_name)


class Books(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    number_of_pages = Column(Integer)

    def __repr__(self):
        return "<Books(book_id='{0}', title = '{1}', number_of_pages='{2}')>".format(self.book_id, self.title, self.number_of_pages)


class BookAuthor(Base):
    __tablename__ = 'bookauthors'
    bookauthor_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    author = relationship("Author")
    book = relationship("Books")

    def __repr__(self):
        return "<BookAuthor (bookauthor_id = '{0}', author_id = '{1}', book_id='{2}',)>".format(self.bookauthor_id, self.author_id, self.book_id)


Base.metadata.create_all(engine)

def add_book(title, number_of_pages, first_name, last_name):
    author = Author(first_name=first_name, last_name=last_name)
    book = Books(title=title, number_of_pages = number_of_pages)

    with Session(engine) as session:
        existing_book = session.execute(select(Books).filter(Books.title==title, Books.number_of_pages==number_of_pages)).scalar()
        if existing_book is not None:
            print("Books Exists! Not adding book")
            return
        print("Books does not exist. Adding book")
        session.add(book)
        existing_author = session.execute(select(Author).filter(Author.first_name==first_name, Author.last_name==last_name)).scalar()
        if existing_author is not None:
            print("Author exists! Not adding the author")
            session.flush()
            pairing = BookAuthor(author_id=existing_author.author_id, book_id=book.book_id)

        else:
            print("Author does not exist. Adding author:")
            session.add(author)
            session.flush()
            pairing = BookAuthor(author_id=author.author_id, book_id=book.book_id)

        session.add(pairing)
        session.commit()
        print("New Pairing added" + str(pairing))


if __name__ == "__main__":
    print("Input new book:\n")
    title = input("What is the title of the book?\n")
    number_of_pages = int(input("How many pages are in the book? \n"))
    first_name = input("What is author's first name?\n")
    last_name = input("What is author's last name?\n")
    print("Inputting the book data:\n")

    add_book(title, number_of_pages, first_name, last_name)

    print("Done!")























