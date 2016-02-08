from django.db import models, transaction
from django.db.models import F
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Ad(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)
    create_time = models.DateTimeField(_('Create time'), auto_now_add=True)
    hits = models.PositiveIntegerField(_('Hits'), blank=True, default=0)

    title = models.CharField(_('Title'), max_length=500)
    description = models.TextField(_('Description'))

    @classmethod
    def hits_plus(cls, ad, user):
        if not user.pk or AdUserHit.objects.filter(ad=ad, user=user).exists():
            return

        with transaction.atomic():
            AdUserHit.objects.create(ad=ad, user=user)
            cls.objects.filter(pk=ad.pk).update(hits=F('hits') + 1)

    @classmethod
    def hits_minus(cls, ad):
        cls.objects.filter(pk=ad.pk).update(hits=F('hits') - 1)

    class Meta:
        ordering = ['-pk']
        verbose_name = _('ad')
        verbose_name_plural = _('ads')

    def __unicode__(self):
        return self.title


class AdUserHit(models.Model):
    ad = models.ForeignKey(Ad)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']


# SIGNALS
@receiver(post_delete, sender=AdUserHit)
def post_ad_user_hit_delete(**kwargs):
    Ad.hits_minus(kwargs['instance'].ad)
