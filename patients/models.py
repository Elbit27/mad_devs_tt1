from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=200, null=False, default='Неизвестно')
    date_of_birth = models.DateField()
    diagnoses = models.JSONField()  # Для хранения списка диагнозов
    created_at = models.DateTimeField(auto_now_add=True)  # Для автоматического указания времени создания

    def __str__(self):
        return f"Patient {self.pk} - {self.full_name}"
