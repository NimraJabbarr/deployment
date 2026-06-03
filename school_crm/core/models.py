from django.db import models   # Django ke ORM (Object Relational Mapper) ko import karte hain

# Student model banaya gaya hai jo database mein ek table create karega
class Student(models.Model):
    name = models.CharField(max_length=100)   # Student ka naam (string field, max 100 characters)
    age = models.IntegerField()               # Student ki age (integer field)
    email = models.EmailField()               # Student ka email (email field, validation ke sath)

    def __str__(self):
        return self.name   # Jab Student object print hoga to uska naam show hoga


# Teacher model banaya gaya hai jo database mein ek table create karega
class Teacher(models.Model):
    name = models.CharField(max_length=100)   # Teacher ka naam (string field, max 100 characters)
    subject = models.CharField(max_length=100) # Teacher ka subject (string field, max 100 characters)
    email = models.EmailField()               # Teacher ka email (email field, validation ke sath)

    def __str__(self):
        return self.name   # Jab Teacher object print hoga to uska naam show hoga
