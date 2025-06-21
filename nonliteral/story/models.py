# story/models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
import uuid


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    connections = models.ManyToManyField('self', through='ChapterConnection', symmetrical=False)
    is_terminal = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_choices(self):
        return Choice.objects.filter(from_chapter=self)

    def get_available_choices(self, reader):
        available_choices = []
        for choice in self.get_choices():
            if reader.money >= abs(choice.money_cost) and reader.energy >= abs(choice.energy_cost):
                available_choices.append(choice)
        return available_choices

    def get_absolute_url(self):
        return reverse('story:chapter_detail', kwargs={'pk': self.pk})

    class Meta:
        app_label = 'story'


class ChapterConnection(models.Model):
    from_chapter = models.ForeignKey(Chapter, related_name='from_chapter_connections', on_delete=models.CASCADE, null=True, default=None)
    to_chapter = models.ForeignKey(Chapter, related_name='to_chapter_connections', on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        unique_together = ('from_chapter', 'to_chapter')
        app_label = 'story'


class Choice(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    money_cost = models.IntegerField(default=0)  # negative = gain
    energy_cost = models.IntegerField(default=0)  # negative = gain
    from_chapter = models.ForeignKey(Chapter, related_name='choices', on_delete=models.CASCADE, default=None, null=True)
    to_chapter = models.ForeignKey(Chapter, related_name='incoming_choices', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f"{self.name} (from {self.from_chapter.title})"

    class Meta:
        app_label = 'story'


class ReaderUser(models.Model):
    """Separate user model for story readers only"""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    # Game-specific fields
    energy = models.IntegerField(default=100)
    money = models.IntegerField(default=100)
    current_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)

    # Meta fields
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    # Session management
    session_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

    def make_choice(self, choice):
        self.money -= choice.money_cost
        self.energy -= choice.energy_cost
        self.current_chapter = choice.to_chapter
        self.save()

    def can_make_choice(self, choice):
        return (self.money >= abs(choice.money_cost) and
                self.energy >= abs(choice.energy_cost))

    def generate_session_token(self):
        """Generate a unique session token"""
        self.session_token = str(uuid.uuid4())
        self.save()
        return self.session_token

    class Meta:
        app_label = 'story'


class UserProgress(models.Model):
    reader = models.ForeignKey(ReaderUser, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    choice_made = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'story'
        ordering = ['-timestamp']
