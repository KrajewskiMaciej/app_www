from rest_framework import serializers
from .models import Category, Topic, Post

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nazwa może zawierać tylko litery!")
        return value

    def validate_created_at(self, value):
        if value > date.today():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości!")
        return value