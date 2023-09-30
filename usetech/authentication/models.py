from django.db import models


class Service(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.name


class Client(models.Model):
    client_id = models.CharField(max_length=256)
    allowed_services = models.ManyToManyField(
        Service,
        through='UserService'
    )

    def __str__(self):
        return self.name


class UserService(models.Model):
    client = models.ForeignKey(
        Client,
        related_name='client',
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(
        Service,
        related_name='allowed_service',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.achievement} {self.cat}'
