from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, GenreDetailSerializer
from .models import Genre, Movie, Review
from rest_framework.response import Response 

# Create your views here.

# 키, 밸류로 구성되는 스트링으로 넘겨야 "serializing"(django-rest framework사용): 바이트 형식
#   -> json으로 만들려면 serializers.py 생성

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET']) # 단순 정보요청: get
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # 검증에 실패하면 400 Bad request 오류를 발생
                            # raise_exception: valid하지 않으면 예외처리하겠닫는 의미
        serializer.save(movie_id=movie_pk, user_id=request.user.pk)  # music_id입력하지 않아도 알아서 저장됨.
                # request.user -> gayoung, request.user.pk=1
    return Response({"message": "작성되었습니다."})


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "수정되었습니다."})

    else:
        review.delete()
    return Response({"message": "삭제되었습니다."})
