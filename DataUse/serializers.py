from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from .models import DataPull_ID, DataPull_Detail

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'content_type_id', 'codename')

#class GroupSerializer(serializers.HyperlinkedModelSerializer):
class GroupSerializer(serializers.ModelSerializer):
    '''
    permissions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='permission-detail'
    )
    '''
    permissions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'groups', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'user_permissions')

# Data Pull stuff
class DataPullIDSerializer(serializers.ModelSerializer):
    pullby = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = DataPull_ID
        fields = ('id', 'pulldate', 'pullname', 'pullquery', 'pulltype', 'pullsource', 'pullby')

class DataPullDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPull_Detail
        fields = ('__all__')