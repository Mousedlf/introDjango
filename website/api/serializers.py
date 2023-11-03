from rest_framework.serializers import ModelSerializer
from website.models import Message, Response, Category, User


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class ResponseSerializer(ModelSerializer):
    class Meta:
        model = Response
        fields = ["id", "content", "author"]
    author = AuthorSerializer()


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    category_ = CategorySerializer(source='category', read_only=True)
    responses = ResponseSerializer(many=True, required=False)
    author = AuthorSerializer(required=False)



