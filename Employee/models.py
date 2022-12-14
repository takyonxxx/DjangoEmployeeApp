from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from mirage import fields


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name="Full Name")
    email = models.EmailField(max_length=99, blank=True, verbose_name="Email")
    username = models.CharField(max_length=255, blank=True, default='')
    password = fields.EncryptedCharField(blank=True, default='')
    is_active = models.BooleanField(default=False, verbose_name="Active")
    created = models.DateTimeField(default=timezone.now)
    REQUIRED_FIELDS = ['name']
    id_prefix = 'emp'

    def __str__(self):
        return self.name

    #
    # def abs_method(self):
    #     raise NotImplementedError()
    #
    class Meta:
        db_table = 'employee'
        ordering = ('-created',)
        # abstract = True

    def save(self, *args, **kwargs):
        try:
            super().full_clean()
            super().save(*args, **kwargs)
        except ValidationError as err:
            raise ValidationError(err)
