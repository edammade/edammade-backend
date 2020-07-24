import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model import Account as AccountModel


class Account(MongoengineObjectType):
    class Meta:
        model = AccountModel
        interfaces = (Node, )


class Query(graphene.ObjectType):
    users = graphene.List(Account)

    def resolve_users(self, info):
        return list(AccountModel.objects.all())


schema = graphene.Schema(query=Query, types=[Account])
