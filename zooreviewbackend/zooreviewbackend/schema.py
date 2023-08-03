import graphene
from graphene_django import DjangoObjectType

from users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "bio", "avatar", "random_string", "verified")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_user_by_name(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
    
schema = graphene.Schema(query=Query)