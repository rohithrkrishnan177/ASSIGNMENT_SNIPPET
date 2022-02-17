from .models import Snippet, Tag
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    TagInfo = serializers.CharField()
    content = serializers.CharField(source='text')
    timestamp = serializers.DateTimeField(source='created')

    class Meta:
        model = Snippet
        fields = ['content', 'timestamp', 'UserInfo','TagInfo', 'id']

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)


class SnippetResolveSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='TagInfo.title')
    content = serializers.CharField(source='text')
    timestamp = serializers.DateTimeField(source='created')

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'timestamp']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"




