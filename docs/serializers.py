from rest_framework import serializers
from .models import Doc

class DocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doc
        fields = (
            "id", 
            "title", 
            "content", 
            "word_count", 
            "char_count",
            "creation_date"
        )