from typing import Iterable

from aiogram.filters import BaseFilter
from aiogram.types import Message


class EntitiesFilter(BaseFilter):
    def __init__(self, entities_types: str | Iterable):
        self.entities_types = entities_types

    async def __call__(self, message: Message) -> bool | dict:
        if isinstance(self.entities_types, str):
            entities = [
                entity.extract_from(message.text) for entity in message.entities if entity.type == self.entities_types
            ]
        else:
            entities = [
                entity.extract_from(message.text) for entity in message.entities if entity.type in self.entities_types
            ]
        if entities:
            return {'filtered_entities': entities}
        return False
