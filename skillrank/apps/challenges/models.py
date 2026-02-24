from django.db import models

# Create your models here.
class Challenge(models.Model):
    DIFFICULTY_LEVELS = [
    ('EASY', 'Easy'),
    ('MEDIUM', 'Medium'),
    ('HARD', 'Hard'),]
    title = models.CharField(max_length=255)
    company = models.ForeignKey('core.Company', on_delete=models.CASCADE, related_name='challenges')
    category = models.CharField(max_length=255, db_index=True)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_LEVELS, default='EASY')
    reward_points = models.IntegerField()
    description = models.TextField()
    requirements = models.TextField()
    required_skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class TestCase(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"TestCase for {self.challenge.title}"