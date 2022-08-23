from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')

    def create(self, validated_data):
        title = self.validated_data['title']
        if Post.objects.filter(title__iexact=title).exists():
            raise serializers.ValidationError("Duplicate")
        post = Post()
        post.author = self.context['request'].user
        post.title = self.validated_data['title']
        post.body = self.validated_data['body']
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
