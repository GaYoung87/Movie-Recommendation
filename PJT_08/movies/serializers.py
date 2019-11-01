from rest_framework import serializers
from .models import Genre, Movie, Review

# 장고에 orm이라는 것은 db에서 data를 꺼내서 장고에 꺼내는 역할
# 장고에 orm은 장고만 알고있는 특정 자료구조.(객체) 그걸 그래도 요청에 담아서 사용자에게 응답을 보내면
# 사용자는 웹페이지만 가지고있지, 장고를 해석할 수 없다.
# 이 데이터를 브라우저에서 해석할 수 있도록 데이터를 변환시키게하는 것.
# JSON타입으로 변환시켜주는 것

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', )


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id', )


# 특정 장르에 대한 영화를 보여준다
class GenreDetailSerializer(GenreSerializer):
    movies = MovieSerializer(many=True)

    class Meta(GenreSerializer.Meta):
        fields = GenreSerializer.Meta.fields + ('movies', )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie_id', 'user_id', )