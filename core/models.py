from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField
from core.format import common_datetime_str


class GenericModel(models.Model):
    id = models.UUIDField(
        verbose_name=_("unique id"),
        primary_key=True,
        unique=True,
        null=False,
        default=uuid4,
        editable=False
    )
    active = models.BooleanField(
        verbose_name=_('active'),
        default=False
    )
    _created_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_created_by",
        verbose_name=_("created by"),
    )
    _updated_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_updated_by",
        verbose_name=_("updated by"),
        on_update=True
    )
    _created_at = models.DateTimeField(
        verbose_name=_('created at'),
        default=timezone.now
    )
    _updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True
    )

    class Meta:
        abstract = True
        indexes = (
            models.Index(fields=['id'], name='%(class)s_id_idx'),
        )

    @property
    def created_by(self):
        if self._created_by:
            return f"{self._created_by.first_name} {self._created_by.last_name}".strip()
        return None

    @property
    def updated_by(self):
        if self._updated_by:
            return f"{self._updated_by.first_name} {self._updated_by.last_name}".strip()
        return None

    @property
    def created_at(self):
        return common_datetime_str(self._created_at)

    @property
    def updated_at(self):
        return common_datetime_str(self._updated_at)
