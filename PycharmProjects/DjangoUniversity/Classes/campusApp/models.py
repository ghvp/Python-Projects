from django.db import models


# Creates model of the university campus
class UniversityCampus(models.Model):
    # specifying the fields for the class and the desired data types
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default=None)

    # creating a model manager
    objects = models.Manager()

    # Displays the campus name and the state
    def __str__(self):
        # returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name}: {0.state}'
        return display_campus.format(self)

    # Making sure that the class is displayed properly as "University Campus" without
    # the added django 's' at the end
    class Meta:
        verbose_name_plural = "University Campus"
