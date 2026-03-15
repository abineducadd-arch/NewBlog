from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import *
from contact.models import *
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","email"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"]
        )
        return user  
    
class GoogleLoginSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get("token")

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                requests.Request(),
                settings.GOOGLE_CLIENT_ID
            )

            email = idinfo.get("email")
            username = email.split("@")[0]

            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=None
                )

            refresh = RefreshToken.for_user(user)

            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }

        except ValueError:
            raise serializers.ValidationError("Invalid Google Token")
        
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBlog
        fields = '__all__'
class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyPost
        fields = '__all__'
class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignPost
        fields = '__all__'
class ProgrammingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingPost
        fields = '__all__'
class LifesyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifestylePost
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
