from .mutations import Mutation
import graphene
from .types import BookType, UserType, LoanType, ReservationType
from ..models.books import Book
from ..models.users import User
from ..models.loans import Loan
from ..models.reservations import Reservation

class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    users = graphene.List(UserType)
    loans = graphene.List(LoanType)
    reservations = graphene.List(ReservationType)

    def resolve_books(self, info):
        return Book.query.all()
    def resolve_users(self, info):
        return User.query.all()
    def resolve_loans(self, info):
        return Loan.query.all()
    def resolve_reservations(self, info):
        return Reservation.query.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
