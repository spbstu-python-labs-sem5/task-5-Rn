class CoordDescriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Координата {self.public_name} должна быть int или float, "
                f"получено {type(value).__name__}"
            )
        instance.__dict__[self.private_name] = value