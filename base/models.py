from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self, deleted_at=None):
        deleted_at = deleted_at or datetime.now()
        self.deleted_at = deleted_at

    def delete_url(self):
        name = self.__class__.__name__.lower()
        return reverse(name + ":delete", kwargs={'pk': str(self.id), })
