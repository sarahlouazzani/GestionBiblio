import graphene
from ..types import BookType
from ...models.books import Book
from ... import db

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        available = graphene.Boolean(required=False)

    book = graphene.Field(lambda: BookType)

    def mutate(self, info, title, author, available=True):
        new_book = Book(title=title, author=author, available=available)
        db.session.add(new_book)
        db.session.commit()
        return CreateBook(book=new_book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        author = graphene.String()
        available = graphene.Boolean()

    book = graphene.Field(lambda: BookType)

    def mutate(self, info, id, **kwargs):
        book = Book.query.get(id)
        if not book:
            raise Exception("Book not found")
        for key, value in kwargs.items():
            setattr(book, key, value)
        db.session.commit()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        book = Book.query.get(id)
        if not book:
            raise Exception("Book not found")
        db.session.delete(book)
        db.session.commit()
        return DeleteBook(ok=True)
