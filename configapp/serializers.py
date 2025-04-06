


from rest_framework import serializers
from configapp.models import Movie, Actors, CommitMovie  # Actors -> Actor


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    year = serializers.IntegerField()
    genre = serializers.CharField()
    photo = serializers.ImageField(required=False, allow_null=True)
    actor = serializers.PrimaryKeyRelatedField(many=True, queryset=Actors.objects.all())

    def create(self, validated_data):
        actors_data = validated_data.pop('actor')
        movie = Movie.objects.create(**validated_data)
        movie.actor.set(actors_data)
        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre', instance.genre)
        if 'actor' in validated_data:
            instance.actor.set(validated_data['actor'])
        instance.save()
        return instance


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    birthdate = serializers.DateField()

    def create(self, validated_data):
        return Actors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        return instance


class CommitSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # token orqali ko‘rsatish uchun

    class Meta:
        model = CommitMovie
        fields = '__all__'






# from rest_framework import serializers
# from configapp.models import Movie, Actors, CommitMovie
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     slug = serializers.SlugField(read_only=True)
#     year = serializers.IntegerField()
#     actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actors.objects.all())
#     genre = serializers.CharField()
#
#     def create(self, validated_data):
#         actors_data = validated_data.pop('actors')
#         movie = Movie.objects.create(**validated_data)
#         movie.actors.set(actors_data)
#         return movie
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.year = validated_data.get('year', instance.year)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.save()
#         return instance
#
#
# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     birth_date = serializers.DateField()
#     slug = serializers.SlugField(read_only=True)  # Agar modelda slug maydoni bo'lsa
#
#     def create(self, validated_data):
#         """
#         Actors obyektini yaratish uchun
#         """
#         return Actors.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Actors obyektini yangilash uchun
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.birth_date = validated_data.get('birth_date', instance.birth_date)
#         instance.save()
#         return instance
#
# class CommitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CommitMovie
#         fields="__all__"