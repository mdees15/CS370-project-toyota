sqlite3 sensor_data.db << "END_OF_SQL"
BEGIN;

INSERT INTO PM25 (timestamp, value) VALUES(datetime('now'), 10.5);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+1 minutes'), 12);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+2 minutes'), 20);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+3 minutes'), 50);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+4 minutes'), 120);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+5 minutes'), 70.12);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+6 minutes'), 501.51);
INSERT INTO PM25 (timestamp, value) VALUES(datetime('now', '+7 minutes'), 0.1);

INSERT INTO PM10 (timestamp, value) VALUES(datetime('now'), 10.5);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+1 minutes'), 12);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+2 minutes'), 20);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+3 minutes'), 50);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+4 minutes'), 40);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+5 minutes'), 2.3);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+6 minutes'), 15.6);
INSERT INTO PM10 (timestamp, value) VALUES(datetime('now', '+7 minutes'), 0.5);

COMMIT;
END_OF_SQL