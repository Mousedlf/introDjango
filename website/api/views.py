from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from website.api.serializers import MessageSerializer
from website.models import Message, User, Category


@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)


@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)


@api_view(['POST'])
def new_message(request):
    if request.method == "POST":
        message = Message()
        message.author = User.objects.get(id=1)
        serialized_message = MessageSerializer(instance=message, data=request.data)
        if serialized_message.is_valid():
            serialized_message.save()
            return Response(serialized_message.data, status=status.HTTP_201_CREATED)

        return Response(serialized_message.errors, status=status.HTTP_400_BAD_REQUEST)
