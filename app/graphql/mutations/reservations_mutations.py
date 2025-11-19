import graphene
from ..types import ReservationType
from ...models.reservations import Reservation
from ... import db

class CreateReservation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        book_id = graphene.ID(required=True)

    reservation = graphene.Field(lambda: ReservationType)

    def mutate(self, info, user_id, book_id):
        from ...models.users import User
        from ...models.books import Book

        user = User.query.get(user_id)
        if not user:
            raise Exception("User not found")

        book = Book.query.get(book_id)
        if not book:
            raise Exception("Book not found")

        existing_reservation = Reservation.query.filter_by(user_id=user_id, book_id=book_id).first()
        if existing_reservation:
            raise Exception("Reservation already exists for this user and book")

        reservation = Reservation(user_id=user_id, book_id=book_id)
        db.session.add(reservation)
        db.session.commit()
        return CreateReservation(reservation=reservation)
    

class UpdateReservation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        user_id = graphene.ID(required=False)
        book_id = graphene.ID(required=False)

    reservation = graphene.Field(lambda: ReservationType)

    def mutate(self, info, id, user_id=None, book_id=None):
        reservation = Reservation.query.get(id)
        if not reservation:
            raise Exception("Reservation not found")

        if user_id is not None:
            reservation.user_id = user_id
        if book_id is not None:
            reservation.book_id = book_id

        db.session.commit()
        return UpdateReservation(reservation=reservation)


class DeleteReservation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        reservation = Reservation.query.get(id)
        if not reservation:
            raise Exception("Reservation not found")
        db.session.delete(reservation)
        db.session.commit()
        return DeleteReservation(ok=True)
