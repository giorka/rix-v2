from sqlalchemy.orm.decl_api import DeclarativeBase, declared_attr


def to_snake_case(string: str) -> str:
    return ''.join(
        [
            '_' + char.lower() if char.isupper()
            else char
            for char in string
        ]
    ).strip('_')


class IModel(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return to_snake_case(self.__name__.lower().strip('model'))
