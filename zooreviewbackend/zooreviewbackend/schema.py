import graphine
from graphene_django import DjangoObjectType

from zooreviewbackend.users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "bio", "avatar", "random_string", "verified")

class Query(graphine.ObjectType):
    all_users = graphine.List(UserType)

    def resolve_user_by_name(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
    
schema = graphine.Schema(query=Query)