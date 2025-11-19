import graphene
from ..types import LoanType
from ...models.loans import Loan
from ... import db

class CreateLoan(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        book_id = graphene.ID(required=True)
        return_date = graphene.String(required=False)

    loan = graphene.Field(lambda: LoanType)

    def mutate(self, info, user_id, book_id, return_date=None):
        from ...models.users import User
        from ...models.books import Book

        user = User.query.get(user_id)
        if not user:
            raise Exception("User not found")

        book = Book.query.get(book_id)
        if not book:
            raise Exception("Book not found")

        existing_loan = Loan.query.filter_by(book_id=book_id, returned=False).first()
        if existing_loan:
            raise Exception("Book is already on loan")

        loan = Loan(user_id=user_id, book_id=book_id, return_date=return_date)
        db.session.add(loan)
        db.session.commit()
        return CreateLoan(loan=loan)
    
class UpdateLoan(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        user_id = graphene.ID(required=False)
        book_id = graphene.ID(required=False)
        return_date = graphene.String(required=False)

    loan = graphene.Field(lambda: LoanType)

    def mutate(self, info, id, user_id=None, book_id=None, return_date=None):
        loan = Loan.query.get(id)
        if not loan:
            raise Exception("Loan not found")
        
        if user_id is not None:
            loan.user_id = user_id
        if book_id is not None:
            loan.book_id = book_id
        if return_date is not None:
            loan.return_date = return_date
        
        db.session.commit()
        return UpdateLoan(loan=loan)

class DeleteLoan(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        loan = Loan.query.get(id)
        if not loan:
            raise Exception("Loan not found")
        db.session.delete(loan)
        db.session.commit()
        return DeleteLoan(ok=True)
