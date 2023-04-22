from rest_framework import serializers
from base.models import quizdata
from django.contrib.auth.models import User

class quizdataserializer(serializers.ModelSerializer):
    class Meta:
        model = quizdata
        fields = ["question","id"]

class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password"]

class addquestionsserializer(serializers.ModelSerializer):
    class Meta:
        model = quizdata
        fields = "__all__"
        