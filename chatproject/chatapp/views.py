from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ModelProvider
from .serializers import ModelProviderSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .llm_stubs import LLMStubManager
from chatapp.models import ModelProvider
from django.shortcuts import render


@api_view(['GET'])
def get_models(request):
    models = ModelProvider.objects.all()
    serializer = ModelProviderSerializer(models, many=True)
    model_names = [model["provider_name"]+"/"+model["model_name"] for model in serializer.data]  
    return Response(model_names)

@csrf_exempt
def chat_completions(request):
    """API endpoint to process chat completions."""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        provider_name = data.get("provider")  
        model_name = data.get("model") 
        prompt = data.get("prompt")

        if not provider_name or not model_name or not prompt:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        # Validation of provider and model in DB
        if not ModelProvider.objects.filter(provider_name=provider_name, model_name=model_name).exists():
            return JsonResponse({"error": "Invalid provider or model"}, status=400)

        response = LLMStubManager.get_response(provider_name, model_name, prompt)

        return JsonResponse(response, safe=False) 

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


def chat_view(request):
    return render(request, "chat.html")
