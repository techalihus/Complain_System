from django.db import models

# Create your models here.

# ==========================
# Designation Model
# ==========================
class Designation(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
# ==========================
# Department Model
# ==========================
class Department(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    @property
    def employee_count(self):
        return self.employee_set.count()
    
# ==========================
# Employee Model
# ==========================
class Employee(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
        
    )
    role=models.CharField(max_length=20, choices=ROLE_CHOICES)
    designation=models.ForeignKey(Designation, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.role} - {self.department}"

# ========================
# Category Model
# =======================
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# =========================
# Ticket Model
class Ticket(models.Model):
    ROLE_CHOICES=(
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'), 
    )
    PRIORITY_CHOICES = (
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
        ('Urgent','Urgent')
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status=models.CharField(max_length=20, choices=ROLE_CHOICES, default='Open')
    title=models.CharField(max_length=200)
    description=models.TextField()
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   

# =========================
# Ticket Reply Model
# =========================
class TicketReply(models.Model):
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Reply by {self.employee} on {self.ticket}'
    
    
# ========================
# TicketRating Model
# =======================
class TicketRating(models.Model):
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField(blank=True, null=True)
    def __str__(self):
        return f'Rating for {self.ticket}: {self.rating}'
    
# ========================
# TicketHistory Model
# =======================
class TicketHistory(models.Model):
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    changed_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'History for {self.ticket}: {self.status} at {self.changed_at}'
    
    @property
    def total_changes(self):
        return TicketHistory.objects.filter(ticket=self.ticket).count()
    
# ========================
#  Notification Model
# =======================
class Notification(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Notification for {self.employee}: {self.message}'
    