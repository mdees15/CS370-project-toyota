#!/bin/bash

sudo apt-get install sqlite3
sqlite3 sensor_data.db << "END_OF_SQL"
BEGIN;
CREATE TABLE PM25 (timestamp DATETIME, value REAL);
CREATE TABLE PM10 (timestamp DATETIME, value REAL);
COMMIT;
END_OF_SQL