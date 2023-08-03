import graphine
from graphene_django import DjangoObjectType

from zooreviewbackend.users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "bio", "avatar", "random_string", "verified")

class Query(graphine.ObjectType):
    all_users = graphine.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.select_related("user").all()
    
schema = graphine.Schema(query=Query)