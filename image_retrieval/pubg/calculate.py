from image_retrieval.box import BoundingBox
from image_retrieval.parse import get_labels


def filter_single_comma(text: str) -> int | str:
    if text.count(",") == 1:
        text = text.replace(",", "")

    if text.isdigit():
        return int(text)

    return text.strip()


def hasalpha(text: str) -> bool:
    for char in text:
        if char.isalnum():
            return True

    return False


def is_end(token: str) -> bool:
    stop_words = ["REWARD", "EXIT", "-", "TO", "LOBBY", "PING", "PLAYER"]

    if token in stop_words:
        return True
    if "NEXT" in token:
        return True
    if token.count(".") > 2:
        return True

    return False


def parse_labels(bounding_boxes: list[BoundingBox]) -> tuple[list[str | int], bool]:
    labels = get_labels(bounding_boxes=bounding_boxes)
    victory = True

    if "DEFEAT" in labels:
        victory = False

    parsed_labels: list[str | int] = []

    for label in labels:
        if "[" in label and "]" in label:
            tokens = label.split(" ")
            parsed_labels.append(" ".join(tokens[:2]))
            tokens = tokens[2:]

        else:
            tokens = label.split(" ")

        for token in tokens:
            if len(token) < 1:
                continue
            if token.isdigit():
                parsed_labels.append(int(token))
            else:
                parsed_labels.append(filter_single_comma(text=token))

    idx = 0
    cnt = 0
    for i, label in enumerate[str | int](parsed_labels):  # type: ignore[assignment]
        if isinstance(label, str) and label == "Score":
            idx = i
            cnt += 1
            if cnt == 2:
                break
    parsed_labels = parsed_labels[idx + 1 :]

    idx = -1

    for i, label in enumerate[str | int](parsed_labels):  # type: ignore[assignment]
        if isinstance(label, str) and is_end(token=label):
            idx = i
            break

    return parsed_labels[:idx], victory


def get_stats_from_parsed_labels(parsed_labels: list[str | int]) -> list[list[str | int]]:
    row: list[str | int] = []
    rows: list[list[str | int]] = []
    start = True
    for label in parsed_labels:
        if len(row) == 5:
            rows.append(row)
            row = [str(label)]
        elif isinstance(label, str):
            if start:
                start = False
            else:
                if len(row) < 5:
                    nones = [-1] * (5 - len(row))
                    row = [row[0]] + nones + row[1:]
                rows.append(row)

            row = [label]
        else:
            row.append(label)

    return rows
