from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import Field, MajorField


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
