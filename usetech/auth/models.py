from django.db import models


class Service(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.name


class UserService(models.Model):
    client = models.ForeignKey(
        related_name='client'
    )
    service = models.ForeignKey(
        related_name='allowed_service'
    )

    def __str__(self):
        return f'{self.achievement} {self.cat}'


class Client(models.Model):
    client_id = models.CharField(max_length=256)
    secret = models.CharField()
    allowed_services = models.ManyToManyField(
        Service,
        through='UserService'
    )

    def __str__(self):
        return self.name