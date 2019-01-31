from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only = True)
	Name = serializers.CharField(max_length = 200)
	Release_date = serializers.DateTimeField()

	Game_category = serializers.CharField(max_length = 200)
	Played = serializers.BooleanField(required = False)

	def create(self, validated_data):
		return Game.objects.creat(**validated_data)

	def update(self, instance, validated_data):
		instance.Name = validated_data.get('Name',instance.Name)
		instance.Release_date = validated_data.get('Release_date',instance.Release_date)
		instance.Game_category = validated_data.get('Game_category',instance.Game_category)
		instance.Played = validated_data.get('Played',instance.Played)
		instance.saved()

		return instance