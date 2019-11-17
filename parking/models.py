from django.db import models

# The status possibilities of the parking spot
STATUS_CHOICES = [
    ("Taken", "Taken"),
    ("Open", "Open"),
    ("Reserved", "Reserved")
]

# Model for a parking spot item
class ParkingSpot(models.Model):
    class Meta:
        app_label = 'parking'

    # The status of the parking spot
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    # model methods
    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status
        }