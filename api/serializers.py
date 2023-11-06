from books.models import Book, Commentary, Genre, Author
from rest_framework import serializers

        
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'number_of_pages', 'price', 'release_date']
        
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance):
        validated_data = self.data
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.price = validated_data.get('price', instance.price)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
