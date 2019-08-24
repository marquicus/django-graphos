""" Model Plot Data Handler"""
from .simple import SimpleDataSource


def get_field_values(row, fields):
    data = []
    for field in fields:
        value = getattr(row, field)
        data.append(value if not callable(value) else value())
    return data


def get_dict_values(row, fields):
    data = []
    for field in fields:
        data.append(row.get(field))
    return data


class ModelDataSource(SimpleDataSource):
    """
    Normalizes data contained in a queryset to format usable by renderers
    """

    def __init__(self, queryset, fields=None):
        """
        : param queryset: :type Django ORM queryset
        : param fields: :type  list of strings
        Example usage:
            # Option 1 - Model instances
            queryset = Account.objects.all()
            mds = ModelDataSource(queryset, fields=['year', 'sales', 'expenses'])

            # Option 2 - Dict instances
            Account.objects.extra(select={'day': 'date( created )'}).values('day').annotate(count=Count('pk'))
            mds = ModelDataSource(queryset, fields=['day', 'count'])

            # This assumes the following model Account:
            class Account(models.Model):
                year = models.IntegerField()
                sales = models.DecimalField()
                expenses = models.DecimalField()
                profit = models.DecimalField()
                created = models.DateTimeField(auto_now_add=True)
        """
        self.queryset = queryset
        self._data_method = get_field_values
        if fields:
            self.fields = fields

        if queryset.exists():
            if isinstance(queryset.first(), dict):
                self.fields = list(queryset.first().keys())
                self._data_method = get_dict_values
            else:
                self.fields = [el.name for el in self.queryset.model._meta.fields]

        self.data = self.create_data(self._data_method)

    def create_data(self, method=get_field_values):
        data = [self.fields]
        for row in self.queryset:
            data.append(method(row, self.fields))
        return data
