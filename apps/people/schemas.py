# Python imports
import graphene

# Django imports

# Third party apps imports
from graphene_django import DjangoObjectType

# Local imports
from .models import Person, Document


# Create your schemas here.
class PersonSchema(DjangoObjectType):
    class Meta:
        model = Person


class PersonQuery(graphene.AbstractType):
    persons = graphene.List(PersonSchema)

    @graphene.resolve_only_args
    def resolve_persons(self):
        return Person.objects.all()


class DocumentSchema(DjangoObjectType):
    class Meta:
        model = Document


class DocumentQuery(graphene.AbstractType):
    documents = graphene.List(DocumentSchema)

    @graphene.resolve_only_args
    def resolve_documents(self):
        return Document.objects.all()
