"""
Define ORM classes.
"""
from sqlobject import *

class RiskType(SQLObject):
    """Define RiskType ORM class."""
    riskTypeName = StringCol()
    fields = RelatedJoin('Field')

class Field(SQLObject):
    """Define Field ORM class."""
    fieldName = StringCol()
    fieldType = ForeignKey('FieldType')
    risks = RelatedJoin('RiskType')

class FieldType(SQLObject):
    """Define FieldType ORM class."""
    fieldTypeName = StringCol()

def create_tables():
    """Create tables in database."""
    RiskType.createTable()
    Field.createTable()
    FieldType.createTable()
