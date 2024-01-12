from pages.base_shape import Base

class InventoryPage(Base):
    iventory_container = ('id', 'inventory_container')

    def is_loaded(self):
        return self.find(self.iventory_container).is_displayed()
