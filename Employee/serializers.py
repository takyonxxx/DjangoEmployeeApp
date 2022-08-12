from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    desc = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'
        # exclude = ('name',)

    def get_desc(self, obj):
        return f'id : {obj.id}, name : {obj.name}, status : {obj.status}'
