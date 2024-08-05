import pygame


class InterfaceObject:
    _object_pull: list = []

    def __init__(self):
        InterfaceObject._object_pull.append(self)

    @classmethod
    def get_items(cls):
        return iter(cls._object_pull)


def handle_interface_objects_click(event: pygame.event.Event):
    for obj in InterfaceObject.get_items():
        if hasattr(obj, "handle_click"):
            obj.handle_click(event)


def draw_interface_objects(screen: pygame.Surface):
    for obj in InterfaceObject.get_items():
        if hasattr(obj, "draw"):
            obj.draw(screen)
