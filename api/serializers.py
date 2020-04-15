from rest_framework import serializers
from data.models import DataContinent, DataCountry, DataCity

class ContinentSerializer(serializers.ModelSerializer):

    # countries = serializers.StringRelatedField(many=True, read_only=True)
    # countries = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = DataContinent
        # fields = ['iso_code', 'name', 'countries']
        fields = ['iso_code', 'name']
    

class CountrySerializer(serializers.ModelSerializer):

    cities = serializers.StringRelatedField(many=True, read_only=True)
    # cities = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = DataCountry
        fields = ['iso_code', 'name', 'cities']
    
    
class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = DataCity
        fields = ['name','type']
