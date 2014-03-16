# -*- coding: utf-8 -*-
"""Class that represent the database structure"""

from sqlalchemy import Column, Integer, String, Boolean, PickleType
from maraschino.database import Base

class Module(Base):
    """Table for one Maraschino module"""
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    column = Column(Integer)
    position = Column(Integer)
    poll = Column(Integer)
    delay = Column(Integer)

    def __init__(self, name, column, position=None, poll=None, delay=None):
        self.name = name
        self.column = column
        self.position = position
        self.poll = poll
        self.delay = delay

    def __repr__(self):
        return '<Module %r>' % (self.name)


class Setting(Base):
    """Table for one setting value"""
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True)
    value = Column(String(500))

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Setting %r>' % (self.key)


class Application(Base):
    """Table for one application in the applications module"""
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(1000))
    description = Column(String(100))
    image = Column(String(100))
    position = Column(Integer)

    def __init__(self, name, url, description=None, image=None, position=None):
        self.name = name
        self.url = url
        self.description = description
        self.image = image

        if position == None:
            self.position = highest_position(Application)
        else:
            self.position = position

    def __repr__(self):
        return '<Application %r>' % (self.name)


class HardDisk(Base):
    """Table for one disk in the diskspace module"""
    __tablename__ = 'disks2'
    id = Column(Integer, primary_key=True)
    data = Column(PickleType)
    position = Column(Integer)


    def __init__(self, data={}, position=None):
        self.data = data

        if position == None:
            self.position = highest_position(HardDisk)
        else:
            self.position = position

    def __repr__(self):
        return '<HardDisk %r>' % (self.position)


class Script(Base):
    __tablename__ = 'scripts'
    id = Column(Integer, primary_key=True)
    label = Column(String(500))
    script = Column(String(500))
    parameters = Column(String(500))
    updates = Column(Integer)
    status = Column(String(500))
    data = Column(PickleType)

    def __init__(self, label, script, parameters=None, updates=0, status=None, data=None):
        self.label = label
        self.script = script
        self.parameters = parameters
        self.updates = updates
        self.status = status
        self.data = data

    def __repr__(self):
        return '<Script %r>' % (self.label)


class NewznabSite(Base):
    __tablename__ = 'newznab'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(100))
    apikey = Column(String(100))


    def __init__(self, name, url, apikey):
        self.name = name
        self.url = url
        self.apikey = apikey

    def __repr__(self):
        return '<NewznabSite %r>' % (self.name)


def highest_position(model):
    highest_position = 0

    items = model.query.all()

    for item in items:
        if item.position > highest_position:
            highest_position = item.position

    return highest_position + 1
