from rest_framework.serializers import ModelSerializer
from website.models import Message, Response, Category, User


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ResponseSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Response
        fields = ["id", "content", "author"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class MessageSerializer(ModelSerializer):
    category = CategorySerializer()
    responses = ResponseSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Message
        fields = '__all__'



