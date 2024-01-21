from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World, WebWorld

WORLD_VERSION = (0, 0, 0)


class TemplateWebWorld(WebWorld):
    pass


class TemplateWorld(World):
    """Phar's template world for bootstrapping an APWorld implementation."""
    game = "Template APWorld"
    web = TemplateWebWorld
    item_id_to_name = {}
    location_id_to_name = {}

    def create_item(self, name: str) -> Item:
        return Item(name, ItemClassification.filler, self.item_id_to_name[name], self.player)

    def fill_slot_data(self) -> dict:
        return {
            "world_version": WORLD_VERSION
        }
