from rest_framework import serializers

from app.models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at']
