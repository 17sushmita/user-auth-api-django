from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Creates a new user.
    Email, username, name and password are required.
    """

    # The password must be validated and should not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'name', 'phone_number', 'token',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """
    Authenticates an existing user.
    Email and password are required.
    """
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    name = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    phone_number = serializers.CharField(max_length=17, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates user data.
        """
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'username': user.get_username,
            'name': user.get_full_name,
            'email': user.get_email_field_name,
            'phone_number': user.get_phone_number,
            'token': user.token,
        }