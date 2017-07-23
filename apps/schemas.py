# Python imports
import graphene

# Django imports

# Third party apps imports
from graphene_django.debug import DjangoDebug

# Local imports
from .people.schemas import DocumentQuery, PersonQuery


# Create your schemas here.
class Query(DocumentQuery, PersonQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
