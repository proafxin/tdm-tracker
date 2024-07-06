from easyocr import Reader

from backend.models.game import Game
from backend.responses.game import GameRequest, GameResponse
from backend.responses.record import RecordRequest, RecordResponse
from backend.service.record import create_new as create_new_record
from image_retrieval.parse import parse_image
from image_retrieval.pubg.calculate import get_stats_from_parsed_labels, parse_labels


def create_new(game_request: GameRequest) -> Game:
    game = Game(**game_request.model_dump())
    game.save()
    game.refresh_from_db()

    return game


def get_by_id(id: int) -> Game | None:
    try:
        game = Game.objects.get(pk=id)
        return game

    except Game.DoesNotExist:
        return None


def get_by_name(name: str) -> Game | None:
    try:
        game = Game.objects.get(name=name)
        return game
    except Game.DoesNotExist:
        return None


def get_pubg_stats_from_image(image_path: str) -> list[RecordResponse]:
    bounding_boxes = parse_image(image_path=image_path, reader=Reader(lang_list=["en"]))
    parsed_labels = parse_labels(bounding_boxes=bounding_boxes)
    stats = get_stats_from_parsed_labels(parsed_labels=parsed_labels)
    game_obj = get_by_name(name="PUBG")
    game = GameResponse(**game_obj.__dict__)

    response: list[RecordResponse] = []
    for stat in stats:
        record_request = RecordRequest(
            game_id=game.id,
            name=str(stat[0]),
            kill=int(stat[1]),
            assist=int(stat[2]),
            death=int(stat[3]),
            point=int(stat[4]),
        )
        record = create_new_record(record_request=record_request)
        response.append(RecordResponse(**record.__dict__))

    return response
