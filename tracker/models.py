from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from datetime import date, timedelta
from django.db.models import Sum

class CustomUser(AbstractUser):
    profile_name = models.CharField(max_length=30)
    profile_description = models.TextField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)

    def __str__(self):
        return self.username

class Habit(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='user'
    )
    title = models.CharField(max_length=50)
    slug =  models.SlugField(
        default='',
        editable=False,
        )
    created_date = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    habit_achieved = models.BooleanField(default=False)
    total_number = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        blank=True,
        null=True
        )
    number_per_day = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        blank=True
    )
    supporters = models.ManyToManyField(
        to='Supporter',
        blank=True,
        related_name='supporter'
    )

    def __str__(self):
        return self.title 

    @property
    def total_completed(self):
        return self.habit_log.aggregate(Sum('log_number_completed'))['log_number_completed__sum']

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        #sets end date on habit
        d = timedelta(days=20)
        if not self.id:
            self.end_date=self.start_date + d
        super().save(*args, **kwargs)
        
class Log(models.Model):
    log_number_completed = models.DecimalField(
        max_digits=9, 
        decimal_places=2,
        blank=True,
        null=True
    )
    log_detail = models.CharField(
        max_length=255,
        blank=True
    )
    habit = models.ForeignKey(
        to=Habit,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='habit_log'
    )
    log_date = models.DateField()
    
    class Meta:
        ordering = ["log_date"]
    
    def __str__(self):
        return self.log_detail

    # boolean to test if log date is <= today's date. then use to display the log in the template
    @property
    def is_visible(self):
        return self.log_date <= date.today()

class Comment(models.Model):
    log = models.ForeignKey(
        to=Log,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='log_comments'
    )
    comment_body = models.CharField(max_length=255)
    comment_date = models.DateField(null=True)

    class Meta:
        ordering = ["comment_date", "id"]

    def __str__(self):
        return self.comment_body


class Supporter(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='user_supporter'
    )
    accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=64)

    def __str__(self):
        return self.user.username 
    

@receiver(post_save, sender=Habit)
def create_log(sender, instance, created, **kwargs):
    if created:
        for i in range(21):
            d = timedelta(days=i)
            l = Log(habit=instance, log_date=instance.start_date + d)
            l.save()

