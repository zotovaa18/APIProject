from django.db import models

# Create your models here.


class Video(models.Model):
    id_ex = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name_video = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'video'

    def __str__(self):
        return self.name_video


class VideoCommands(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    id_v = models.ForeignKey(Video, models.DO_NOTHING, db_column='id_v')
    command = models.TextField()
    num = models.DecimalField(max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'video_commands'

    def __str__(self):
        return self.id
