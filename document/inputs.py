import graphene

class DocumentInput(graphene.InputObjectType):
    owner = graphene.Int()
    name = graphene.String()

