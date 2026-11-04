from functools import lru_cache

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
        
@lru_cache(maxsize=None)
def make_point_class(n, name=None):

    class_name = name or "PointN"

    namespace = {}
    for i in range(n):
        namespace[f"x{i}"] = CoordDescriptor()

    def to_tuple(self):
        return tuple(getattr(self, f"x{i}") for i in range(n))

    namespace["to_tuple"] = to_tuple

    args = ", ".join(f"x{i}" for i in range(n))
    assigns = "\n        ".join(f"self.x{i} = x{i}" for i in range(n))
    init_src = f"def __init__(self, {args}):\n        {assigns}\n"
    init_globals = {}
    exec(init_src, init_globals)
    namespace["__init__"] = init_globals["__init__"]

    return type(class_name, (), namespace)