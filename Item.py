class Item:
    def __init__(self, item_id, position, size):
        self.item_id = item_id
        self.position = position
        self.size = size

    def __repr__(self):
        return f"Item(id={self.item_id}, position={self.position}, size={self.size})"