from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from website.api.serializers import MessageSerializer
from website.models import Message, User, Category


@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_message(request):
    if request.method == "POST":
        message = Message()
        message.author = request.user
        serialized_message = MessageSerializer(instance=message, data=request.data)
        if serialized_message.is_valid():
            serialized_message.save()
            return Response(serialized_message.data, status=status.HTTP_201_CREATED)

        return Response(serialized_message.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_message(request, id):
    message = Message.objects.get(id=id)

    if message.author != request.user:
        return Response("not yours to change")

    if request.method == "POST":
        serialized_message = MessageSerializer(instance=message, data=request.data)
        if serialized_message.is_valid():
            serialized_message.save()
            return Response(serialized_message.data, status=status.HTTP_201_CREATED)

    return Response("nothing to see here")


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_message(request,id):
    Message.objects.filter(id=id).delete()
    return Response("deleted")


@api_view(['POST'])
def register_user(request):
    return None
