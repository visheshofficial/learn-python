from django.db.models import (
    CharField,
    SlugField,
    TextField,
    DateField,
    ManyToManyField,
    ManyToOneRel,
    Model,
)
from organizer.models import Tag, Startup


class Post(Model):
    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    text = TextField()
    pub_date = DateField()
    tags = ManyToManyField(Tag)
    startups = ManyToManyField(Startup)

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]

    def __str__(self):
        date_str = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_str}"
