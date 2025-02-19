from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ModelProvider
from .serializers import ModelProviderSerializer

@api_view(['GET'])
def get_models(request):
    models = ModelProvider.objects.all()
    serializer = ModelProviderSerializer(models, many=True)
    model_names = [model["provider_name"]+"/"+model["model_name"] for model in serializer.data]  
    return Response(model_names)
