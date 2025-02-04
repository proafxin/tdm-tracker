from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    Index,
    IntegerField,
)

from backend.models.base import Base
from backend.models.games import Game


class Record(Base):
    game = ForeignKey(to=Game, on_delete=CASCADE)
    victory = BooleanField()
    date = DateField()
    name = CharField(max_length=100, null=False)
    kill = IntegerField(default=-1)
    assist = IntegerField(default=-1)
    death = IntegerField(default=-1)
    point = IntegerField(default=-1)

    class Meta:
        indexes = [
            Index(fields=["name"]),
            Index(fields=["date"]),
            Index(fields=["name", "game_id"]),
            Index(fields=["created_at"]),
            Index(fields=["updated_at"]),
        ]
