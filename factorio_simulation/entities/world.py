# from factorio_simulation.entities.entity import Entity
# from factorio_simulation.entities.tile import Tile
# import numpy
#
#
# class World(Entity):
#
#     def __init__(self, id):
#         self.width = 0
#         self.height = 0
#         self.map = self.__build_map(id, self.width, self.height)
#         super().__init__(id)
#
#     def __build_map(self, width, height):
#         vectorized = numpy.array([Tile(69) for i in range(width * height)])
#         dimensionalized_map = vectorized.reshape(width, height)
#         return dimensionalized_map
#
#     @classmethod
#     def from_map_dimensions(cls, id, width, height):
#         cls.width = width
#         cls.height = height
#         cls.map = cls.__build_map(cls, width, height)
#
#         super().__init__(cls, id)
