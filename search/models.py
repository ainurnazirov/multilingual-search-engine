from django.db import models

class Query(models.Model):
    query = models.TextField(null = True)
    n_result = models.IntegerField(null = True)
    query_t = models.TextField(null = True)
    n_result_t = models.IntegerField(null = True)
    increase = models.IntegerField(null = True)
    search_time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.query
