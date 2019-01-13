from django.db import models
import json

class Project(models.Model):

    # Name of the project (primary key)
    name = models.CharField(max_length = 64, primary_key = True, default = 'Project')

    # Importance of the project used for sorting
    importance = models.PositiveSmallIntegerField()

    # Visual representation of the project
    image = models.ImageField(upload_to = 'images/projects/')

    # Short summary of the project on the main page
    summary = models.CharField(max_length = 128)

    # Long description of the project when clicked
    description = models.TextField()

    # List of technologies used, stored as a JSON string in the DB
    technologies = models.CharField(max_length = 256)

    def set_technologies(self, list):
        self.technologies = json.dumps(list)

    def get_technologies(self):
        return json.loads(self.technologies)

    # Link to project (generally it's a github repo, but could be different)
    link = models.URLField()
