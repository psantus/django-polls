from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from django.db import connection


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # Generate ID manually
            with connection.cursor() as cursor:
                cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM auth_user")
                self.pk = cursor.fetchone()[0]
        super().save(*args, **kwargs)


# Monkey-patch ContentType to auto-generate IDs
_original_contenttype_save = ContentType.save

def contenttype_save_with_id(self, *args, **kwargs):
    if not self.pk:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM django_content_type")
            self.pk = cursor.fetchone()[0]
    _original_contenttype_save(self, *args, **kwargs)

ContentType.save = contenttype_save_with_id


# Monkey-patch LogEntry to auto-generate IDs
_original_logentry_save = LogEntry.save

def logentry_save_with_id(self, *args, **kwargs):
    if not self.pk:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COALESCE(MAX(id), 0) + 1 FROM django_admin_log")
            self.pk = cursor.fetchone()[0]
    _original_logentry_save(self, *args, **kwargs)

LogEntry.save = logentry_save_with_id
