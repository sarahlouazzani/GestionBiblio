import graphene
from ..types import UserType
from ...models.users import User
from ... import db

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, id, **kwargs):
        user = User.query.get(id)
        if not user:
            raise Exception("User not found")
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        user = User.query.get(id)
        if not user:
            raise Exception("User not found")
        db.session.delete(user)
        db.session.commit()
        return DeleteUser(ok=True)
