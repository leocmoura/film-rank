from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('user'),

class RecommendedMovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    genre = serializers.CharField()
    
    class Meta:
        model = Movie
        fields = '__all__'