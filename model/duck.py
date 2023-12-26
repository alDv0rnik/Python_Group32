from enum import Enum


class DuckType(Enum):
    MELLARD = "mellard"
    DOMESTIC_DUCK = "domestic duck"
    SCROOGE_MCDUCK = "scrooge mcduck"


COLOR_BY_TYPE_MAPPING = {
    DuckType.MELLARD: "brown",
    DuckType.DOMESTIC_DUCK: "white",
    DuckType.SCROOGE_MCDUCK: "money"
}


class Duck:
    def __init__(self, duck_type: DuckType):
        self._type = duck_type
    
    @property
    def color(self):
        return COLOR_BY_TYPE_MAPPING.get(self._type)
    
    def fly(self):
        if self._type != DuckType.SCROOGE_MCDUCK:
            return "FLY"
        else:
            return "MONEY"
