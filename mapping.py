from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import decimal
from sqlalchemy import Column, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Holds the energy data (KWH generated at every time interval)
class EnergyData(Base):
    __tablename__ = 'EnergyData'
    id = Column('time' ,Time, primary_key=True)
    intervalEnergy = Column('intervalEnergy', DECIMAL)

# Holds username and password
class accountDetails(Base):
    __tablename__ = 'AccountDetails'
    id = Column('username', VARCHAR(20), primary_key=True)
    password = Column('password', VARCHAR(20))

# Hold the admin-set default settings for the webpage
class DasboardSettings(Base):
    __tablename__ = 'DashboardSettings'
    timeScale = Column('timescale', VARCHAR(10), primary_key=True)
    pricePerKWh = Column('pricePerKwh', DECIMAL)

# Stores all info necessary for calculating and displaying the analogy
class EnergyAnalogy(Base):
    __tablename__ = 'EnergyAnalogy'
    string1 = Column(VARCHAR(100), primary_key=True)
    string2 = Column(VARCHAR(100))
    energyUnit = Column(DECIMAL)
    imageURL = Column(VARCHAR(100))

