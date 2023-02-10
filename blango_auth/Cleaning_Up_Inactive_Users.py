from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from blango_auth.models import User
User.objects.filter(
    is_active=False,
    date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
).delete()