from uuid import UUID, uuid4


class Component:

    def __init__(self):
        self.component_id: UUID = uuid4()

    def __hash__(self):
        return hash(type(self))

    def to_dict(self):
        raise NotImplementedError(
            self.__class__.__name__ + " has not implemented to_dict"
        )
