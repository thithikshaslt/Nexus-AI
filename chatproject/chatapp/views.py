from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ModelProviderSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from .llm_stubs import LLMStubManager
from chatapp.models import ModelProvider, RoutingRule
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_models(request):
    models = ModelProvider.objects.all()
    serializer = ModelProviderSerializer(models, many=True)
    model_names = [model["provider_name"]+"/"+model["model_name"] for model in serializer.data]  
    return Response(model_names)


@csrf_exempt
def chat_completions(request):
    """API endpoint to process chat completions with regex-based routing."""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        print("in the chat completion")
        print("rb", request.POST)
        data = json.loads(request.body)
        provider_name = data.get("provider")
        model_name = data.get("model")
        prompt = data.get("prompt")
        print("HEERERERE")

        if not provider_name or not model_name or not prompt:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        if not ModelProvider.objects.filter(provider_name=provider_name, model_name=model_name).exists():
            return JsonResponse({"error": "Invalid provider or model"}, status=400)

        rerouted_model = model_name  
        routing_rules = RoutingRule.objects.filter(original_model=model_name)  
        rerouted = False
        for rule in routing_rules:
            print("here ") 
            if re.search(rule.regex_pattern, prompt, re.IGNORECASE): 
                rerouted = True
                rerouted_model = rule.redirect_model
                print("ok", rerouted_model) 
                provider_name = rerouted_model.split("/")[0]
                break  
        if rerouted:
            response = LLMStubManager.get_response(provider_name, rerouted_model.split("/")[1], prompt)
            response['message'] = "Routed to " + provider_name
        else:
            response = LLMStubManager.get_response(provider_name, rerouted_model, prompt)
            


        return JsonResponse(response, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


def chat_view(request):
    return render(request, "chat.html")

@csrf_exempt
def chat_upload(request):
    if request.method == "POST":
        sender = request.POST.get("sender", "Anonymous")
        message = request.POST.get("message", "")
        file = request.FILES.get("file")

        print("file", file)
        print("mess", message)

        chat_message = ChatMessage(sender=sender, message=message, file=file)
        chat_message.save()

        return JsonResponse({
            "message": message if message else "File uploaded successfully." if file else "",
            "file_url": chat_message.file.url if file else None
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

from .models import FileRoutingRule 

@csrf_exempt
def file_upload(request):
    """Handle file uploads with special routing."""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    if "file" not in request.FILES:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    uploaded_file = request.FILES["file"]
    file_extension = uploaded_file.name.split(".")[-1].upper()  

    routing_rule = FileRoutingRule.objects.filter(file_type=file_extension).first()
    
    if not routing_rule:
        return JsonResponse({"error": f"No routing rule for file type: {file_extension}"}, status=400)

    response_data = {
        "provider": routing_rule.provider,
        "model": routing_rule.model,
        "response": f"{routing_rule.provider}: File processed with secure file analysis. Response ID: {routing_rule.provider}_file_response_004"
    }

    return JsonResponse(response_data, status=200)
