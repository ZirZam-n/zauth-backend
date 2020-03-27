from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import Field, MajorField, City, Country, State, University, ZUser


class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='name')
    state = serializers.CharField(source='state.name')
    country = serializers.CharField(source='state.country.name')

    class Meta:
        model = City
        fields = ['country', 'state', 'city']

    def get_related_object(self, data, raise_exception=True):
        country = Country.objects.filter(name=data.get('state').get('country').get('name'))
        if country.count() != 1:
            if raise_exception:
                raise serializers.ValidationError('Country not found.')
            return None
        country = country.get()

        state = country.state_set.filter(name=data.get('state').get('name'))
        if state.count() != 1:
            if raise_exception:
                raise serializers.ValidationError('State not found.')
            return None
        state = state.get()

        city = state.city_set.filter(name=data.get('name'))
        if city.count() != 1:
            if raise_exception:
                raise serializers.ValidationError('City not found.')
            return None
        city = city.get()

        return city

    def validate(self, data):
        self.get_related_object(data)
        return data

    def create(self, data):
        return self.get_related_object(data)


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name']


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = ZUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            raise ValueError('Passwords do not match.')
        data.pop('password1')
        password = data.pop('password2')
        data.set('password', make_password(password))
        return data

    def create(self, data):
        return ZUser.objects.create(is_active=False, **data)


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['minor', 'major']

    major = serializers.CharField(source='major.name')
    minor = serializers.CharField(source='minor_name')

    def get_related_object(self, data, raise_exception=True):
        major_instance = MajorField.objects.filter(name=data.get('major').get('name'))
        if major_instance.count() != 1:
            if raise_exception:
                raise serializers.ValidationError('Major not found.')
            return None

        major_instance = major_instance.get()
        minor_instance = major_instance.field_set.filter(minor_name=data.get('minor_name'))
        if minor_instance.count() != 1:
            if raise_exception:
                raise serializers.ValidationError('Minor for the given major not found.')
            return None

        return minor_instance.get()

    def validate(self, data):
        self.get_related_object(data)
        return data

    def create(self, data):
        return self.get_related_object(data)
