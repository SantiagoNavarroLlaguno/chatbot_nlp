from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from knowledge_base.models import Solution
from nlp_engine.utils import preprocess_text

class ChatView(APIView):
    def post(self, request, *args, **kwargs):
        user_input = request.data.get("input", "")
        processed_input = preprocess_text(user_input)

        return Response({"response": "Here's a solution to your problem"})
