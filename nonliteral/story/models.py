from django.db import models
from django.contrib.auth.models import AbstractUser


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_starting_chapter = models.BooleanField(default=False)
    is_terminal = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_choices(self):
        return self.choices_from.all()

    def get_available_choices(self, user):
        available_choices = []
        for choice in self.get_choices():
            if user.money + choice.money_cost >= 0 and user.energy + choice.energy_cost >= 0:
                available_choices.append(choice)
        return available_choices

    class Meta:
        app_label = 'story'


class Choice(models.Model):
    text = models.CharField(max_length=255)
    # Negative values mean cost, positive values mean gain
    money_cost = models.IntegerField(default=0)
    energy_cost = models.IntegerField(default=0)
    from_chapter = models.ForeignKey(Chapter, related_name='choices_from', on_delete=models.CASCADE)
    to_chapter = models.ForeignKey(Chapter, related_name='choices_to', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_chapter.title} -> {self.to_chapter.title}: {self.text}"

    class Meta:
        app_label = 'story'
        unique_together = ('from_chapter', 'to_chapter', 'text')


class ReaderUser(AbstractUser):
    energy = models.IntegerField(default=100)
    money = models.IntegerField(default=100)
    current_chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='reader_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='reader_users', blank=True)

    def make_choice(self, choice):
        """Make a choice and update stats"""
        if self.money + choice.money_cost < 0 or self.energy + choice.energy_cost < 0:
            return False

        self.current_chapter = choice.to_chapter
        self.money += choice.money_cost
        self.energy += choice.energy_cost
        self.save()

        # Record the choice in history
        ChoiceHistory.objects.create(
            user=self,
            choice=choice,
            from_chapter=choice.from_chapter,
            to_chapter=choice.to_chapter
        )
        return True

    def reset_adventure(self):
        """Reset user to starting conditions"""
        self.money = 100
        self.energy = 100
        starting_chapter = Chapter.objects.filter(is_starting_chapter=True).first()
        self.current_chapter = starting_chapter
        self.save()
        # Clear history
        ChoiceHistory.objects.filter(user=self).delete()

    class Meta:
        app_label = 'story'


class ChoiceHistory(models.Model):
    """Track user's choices through the story"""
    user = models.ForeignKey(ReaderUser, related_name='choice_history', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    from_chapter = models.ForeignKey(Chapter, related_name='history_from', on_delete=models.CASCADE)
    to_chapter = models.ForeignKey(Chapter, related_name='history_to', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'story'
        ordering = ['-timestamp']
