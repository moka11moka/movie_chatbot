from toolbox.api.serializers.serializers import serializers


class ServiceItemSerializer(serializers.Serializer):

    content = serializers.SerializerMethodField()
    is_system = serializers.SerializerMethodField()

    class Meta:
        fields = ("content", "is_system")

    def create(self, validated_data):
        return super(ServiceItemSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(ServiceItemSerializer, self).update(instance, validated_data)

    def get_content(self, obj):
        return obj.get('content', '')

    def get_is_system(self, obj):
        return True

