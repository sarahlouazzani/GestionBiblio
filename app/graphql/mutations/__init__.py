import graphene
from .books_mutations import CreateBook, UpdateBook, DeleteBook
from .users_mutations import CreateUser, UpdateUser, DeleteUser
from .loans_mutations import CreateLoan, UpdateLoan, DeleteLoan
from .reservations_mutations import CreateReservation, UpdateReservation, DeleteReservation

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_loan = CreateLoan.Field()
    update_loan = UpdateLoan.Field()
    delete_loan = DeleteLoan.Field()

    create_reservation = CreateReservation.Field()
    update_reservation = UpdateReservation.Field()
    delete_reservation = DeleteReservation.Field()
