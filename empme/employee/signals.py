from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Workflow

@receiver(post_save, sender=Employee)
def create_workflow(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'workflow'):
        Workflow.objects.create(employee=instance, company = instance.company)
