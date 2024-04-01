from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Chapter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    connections = models.ManyToManyField('self', through='ChapterConnection', symmetrical=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_connections(self):
    #     return self.connections

    def get_choices(self):
        return Choice.objects.filter(node=self)

    def get_available_choices(self, user):
        available_choices = []
        for choice in self.get_choices():
            if user.money >= choice.money and user.energy >= choice.energy:
                available_choices.append(choice)
        return available_choices

    class Meta:
        app_label = 'story'


class ChapterConnection(models.Model):
    from_chapter = models.ForeignKey(Chapter, related_name='from_chapter_connections', on_delete=models.CASCADE)
    to_chapter = models.ForeignKey(Chapter, related_name='to_chapter_connections', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_chapter', 'to_chapter')


class Choice(models.Model):
    name = models.CharField(max_length=255)
    money = models.IntegerField()
    energy = models.IntegerField()
    node = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'story'


class ReaderUser(AbstractUser):
    energy = models.IntegerField(default=100)
    money = models.IntegerField(default=100)
    current_node = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)

    groups = models.ManyToManyField('auth.Group', related_name='reader_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='reader_users')

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def make_choice(self, choice):
        self.current_node = choice.node
        self.money -= choice.money
        self.energy -= choice.energy
        self.save()

    class Meta:
        app_label = 'story'
