from django.db import models


class Category(models.Model):

    __tablename__ = 'category'

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Profits(models.Model):

    __tablename__ = 'profits'

    count = models.IntegerField(null=False)
    date_profit = models.DateField('date to profits')


class Costs(models.Model):

    __tablename__ = 'costs'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.IntegerField(null=False)
    description = models.TextField(max_length=200, default=None)
    date_costs = models.DateField('date cost')
