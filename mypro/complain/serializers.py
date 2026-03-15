from rest_framework import serializers
from .models import Department, Employee, Category, Ticket, TicketReply, TicketHistory, TicketRating,Notification, Designation

# =========================
#  Department Serializer
# =========================
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"
# ========================
# Designation Serializer
# ========================
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields="__all__"
# =========================
# Employee Serializer
# =========================
class EmployeeSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer(read_only=True)
    department_id=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', write_only=True)
    designation = DesignationSerializer(read_only=True)
    designation_id = serializers.PrimaryKeyRelatedField(
    queryset=Designation.objects.all(),
    source="designation",
    write_only=True
)
    class Meta:
        model=Employee
        fields="__all__"


# ========================
#  Category Serializer
# ========================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

# ========================
# Ticket Serializer
# ========================
class TicketSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    category_id=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category',
    write_only=True)
    employee=EmployeeSerializer(read_only=True)
    employee_id=serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee',
    write_only=True)
    reply_count = serializers.IntegerField(read_only=True)
    class Meta:
        model=Ticket
        fields="__all__"

# ========================
# Ticket Reply Serializer
# ========================
class TicketReplySerializer(serializers.ModelSerializer):
    ticket=TicketSerializer(read_only=True)
    ticket_id=serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), source='ticket', write_only=True)
    employee=EmployeeSerializer(read_only=True)
    employee_id=serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)
    class Meta:
        model=TicketReply
        fields="__all__"

# ========================
# Ticket History Serializer
# ========================
class TicketHistorySerializer(serializers.ModelSerializer):
    ticket=TicketSerializer(read_only=True)
    ticket_id=serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), source='ticket', write_only=True)
    changed_by = EmployeeSerializer(read_only=True)
    changed_by_id = serializers.PrimaryKeyRelatedField(
    queryset=Employee.objects.all(),
    source="changed_by",
    write_only=True
)
    class Meta:
        model=TicketHistory
        fields="__all__"

# ========================
# Ticket Rating Serializer
# ========================
class TicketRatingSerializer(serializers.ModelSerializer):
    ticket=TicketSerializer(read_only=True)
    ticket_id=serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all(), source='ticket', write_only=True)
    class Meta:
        model=TicketRating
        fields="__all__"

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

# ========================
# Designation Serializer
# ========================
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields="__all__"

# ========================
# Notification Serializer
# ========================
class NotificationSerializer(serializers.ModelSerializer):
    employee=EmployeeSerializer(read_only=True)
    employee_id=serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=True)
    class Meta:
        model=Notification
        fields="__all__"


    
    
