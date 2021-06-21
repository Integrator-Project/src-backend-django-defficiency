from rest_framework import serializers
from api.requests import GithubDataRepoRequest, LinksUrl


class LinksUrlSerializer(serializers.Serializer):
    self = serializers.URLField()
    git = serializers.URLField()
    html = serializers.URLField()

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)

        return instance

    def create(self, validated_data):
        return LinksUrl(**validated_data)


class CountryVaccinationDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    path = serializers.CharField()
    sha = serializers.CharField()
    size = serializers.IntegerField()
    url = serializers.URLField()
    html_url = serializers.URLField()
    git_url = serializers.URLField()
    download_url = serializers.URLField()
    type = serializers.CharField()
    _links = LinksUrlSerializer()

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)

        return instance

    def create(self, validated_data):
        return GithubDataRepoRequest(**validated_data)
