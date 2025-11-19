import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.books import Book
from ..models.users import User
from ..models.loans import Loan
from ..models.reservations import Reservation

class BookType(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node,)

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)

class LoanType(SQLAlchemyObjectType):
    class Meta:
        model = Loan
        interfaces = (graphene.relay.Node,)

class ReservationType(SQLAlchemyObjectType):
    class Meta:
        model = Reservation
        interfaces = (graphene.relay.Node,)
