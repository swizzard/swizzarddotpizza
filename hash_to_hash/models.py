from django.db import models


class Hashtag(models.Model):
    tag = models.CharField(max_length=140)

    def __unicode__(self):
        return self.tag


class Cluster(models.Model):
    hashtags = models.ManyToManyField(to="Hashtag", through="Votes")
    baseline = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.id)


class Votes(models.Model):
    hashtag = models.ForeignKey("Hashtag")
    cluster = models.ForeignKey("Cluster")
    nos = models.IntegerField(default=0)
    seen = models.IntegerField(verbose_name="times_seen", default=0)

    def __unicode__(self):
        return str(self.id)