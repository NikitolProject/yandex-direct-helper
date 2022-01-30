from django.db import models


class LoginsModel(models.Model):
    """
    Модель для хранения логинов.
    """
    login = models.CharField(max_length=255, unique=True)

    def __str__(self: 'LoginsModel') -> str:
        return self.login


class CidModel(models.Model):
    """
    Модель для хранения ключей для получения клиентов.
    """
    login = models.ForeignKey(LoginsModel, on_delete=models.CASCADE)
    cid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self: 'CidModel') -> str:
        return self.name


class UrlsModel(models.Model):
    """
    Модель для хранения ключей для получения клиентов.
    """
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self: 'UrlsModel') -> str:
        return self.name
