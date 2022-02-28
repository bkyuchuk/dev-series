from typing import Any, Callable

Callbacks = list[Callable[..., None]]

subscribers: dict[str, Callbacks] = dict()


def subscribe(event_type: str, fn: Callable[..., None]):
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data: Any):
    if event_type not in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
