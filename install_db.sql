DROP TABLE IF EXISTS relays;
CREATE TABLE relays(id INT, start varchar(5), end varchar(5), name varchar(150), runonce INT, t1 REAL, t2 REAL);
insert into relays values ("0","10:50","11:01", "pierwszy PK", 0, "22,1", "23,3");
insert into relays values ("1","10:51","11:02", "drugi PK", 0, "22,2", "23,4");
insert into relays values ("2","10:52","11:03", "trzeci PK", 0, "22,3", "23,5");
insert into relays values ("3","10:53","11:04", "czwarty PK", 0, "22,4", "23,6");
insert into relays values ("4","10:54","11:05", "piaty PK", 0, "22,5", "23,7");
insert into relays values ("5","10:55","11:06", "szosty PK", 0, "22,6", "23,8");
insert into relays values ("6","10:56","11:07", "siodmy PK", 0, "22,7", "23,9");
insert into relays values ("7","10:57","11:07", "osmy PK", 0, "22,8", "24,0");

