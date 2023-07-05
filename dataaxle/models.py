import datetime
import uuid
from django.db import models, transaction
from django.db.models import Case, When


class SoftDeleteQuerySet(models.QuerySet):
    @transaction.atomic
    def delete(self):
        self.update(deleted=True, updated_on=datetime.datetime.now())

    def hard_delete(self):
        # TODO: Add logger service here
        super(SoftDeleteQuerySet, self).delete()


class BaseManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.with_deleted = kwargs.pop('deleted', False)
        super(BaseManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qs = SoftDeleteQuerySet(self.model)
        if self.with_deleted:
            return qs
        else:
            return qs.filter(deleted=False)

    def filter_with_sequence(self, order_by_pk):
        queryset = super(BaseManager, self).get_queryset()
        preserved = Case(*[When(pk=pk, then=idx) for idx, pk in enumerate(order_by_pk)])
        return queryset.filter(id__in=order_by_pk).order_by(preserved)


class BaseManagerWithArchived(BaseManager):
    def __init__(self, *args, **kwargs):
        self.with_archived = kwargs.pop('archived', False)
        super(BaseManagerWithArchived, self).__init__(*args, **kwargs)

    def get_queryset(self):
        qs = super(BaseManagerWithArchived, self).get_queryset()
        if not self.with_archived:
            qs = qs.filter(archived=False)
        return qs


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = BaseManager()
    all_objects = BaseManager(deleted=True)

    class Meta:
        abstract = True

    def delete(self):
        self.updated_on = datetime.datetime.now()
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)


