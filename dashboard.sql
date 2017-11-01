CREATE DATABASE HeliosDashboard;

CREATE TABLE Energy
(
--Timestamp will be updated when a row is updated every 10 minutes
Timestamp datetime,
EnrgyInterval int
);

CREATE TABLE DisplaySetting
(
DPSetting text
);

CREATE TABLE ADLogin
(
Username text,
Password text
);

CREATE TABLE ENRGYAnalogy
(
string1 text,
string2 text,
EnergyUnit text
);
