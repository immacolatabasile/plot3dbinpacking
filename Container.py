from Item import Item

class Container:
    def __init__(self, container_id, dimensions):
        self.container_id = container_id
        self.dimensions = dimensions
        self.Items = {}

    def add_Item(self, item_id: str, position: list, size: list):
        """Aggiunge un item al container se rientra nei limiti."""
        #if self._is_within_bounds(position, size):
        self.Items[item_id] = Item(item_id, position, size)
        # else:
        #     raise ValueError("Item exceeds container boundaries.")

    def _is_within_bounds(self, position: list, size: list) -> bool:
        """Controlla se l'item è all'interno dei confini del container."""
        for i in range(3):
            if position[i] + size[i] > self.dimensions[i]:
                return False
        return True

    def get_Items(self) -> list:
        return list(self.Items.values())

    def __repr__(self) -> str:
        """Restituisce una rappresentazione in stringa del container."""
        return f"Container(id={self.container_id}, dimensions={self.dimensions}, Items={self.Items})"
