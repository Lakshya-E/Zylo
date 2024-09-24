from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_feilds):
        if not email:
            raise ValueError("User must have email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_feilds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_super(self, email, password=None, **extra_feilds):
        extra_feilds.setdefault("is_staff", True)
        extra_feilds.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_feilds)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    object = UserManager()

    USERNAME_FEILD = 'email'

    def get_full_nam(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.email
    