from rest_framework import serializers
# from account.models import User


class BaseAPIModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(BaseAPIModelSerializer, self).__init__(*args, **kwargs)
        self.request = self.context.get('request', None)
        self.user = self.request.user if self.request else None

    # def has_permission(self, permission_name):
    #     return False if not isinstance(self.user, User) else self.user.has_perm(permission_name)

    def get_errors(self):
        error_dict = dict()
        for field_name, errors in self.errors.items():
            if field_name not in error_dict:
                error_dict[field_name] = []
            for error in errors:
                error_dict[field_name].append(str(error))
        return error_dict


class BaseSelectAPIModelSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = None
        fields = ('id', 'name')

    def get_id(self, obj):
        return obj.id


class ImportErrorSerializer(BaseAPIModelSerializer):

    row = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    class Meta:
        model = None
        fields = ('row', 'reason')

    def __init__(self, *args, **kwargs):
        super(ImportErrorSerializer, self).__init__(*args, **kwargs)
        self.meta_data = None

    def to_representation(self, instance):
        self.meta_data = instance.json_meta_data
        return super(ImportErrorSerializer, self).to_representation(instance)

    def get_row(self, obj):
        return self.meta_data.get('row', '')

    def get_reason(self, obj):
        return self.meta_data.get('reason', '')