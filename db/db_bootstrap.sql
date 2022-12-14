-- going to be used by docker and the container
-- to bootstrap our database server with data
-- and tables and whatever else we put in the file
CREATE DATABASE trainbt;

-- create a user that can access the 'test' database
CREATE USER 'webapp'@'%' IDENTIFIED BY 'tbtDatabase3200';
-- a user that has the password 'tbtDatabase3200'
-- 'webapp'@'%' - the webapp user will be able to connect from any IP address

-- need to tell mySQL that we want this particular user
-- to have access to this database called 'trainbt'
GRANT ALL PRIVILEGES ON trainbt.* TO 'webapp'@'%';

-- privileges need to take effect in the database
FLUSH PRIVILEGES;

-- tell mySQL what database we are going to be using
USE trainbt;

CREATE TABLE passengers (
    passengerID integer,
    firstName varchar(50),
    lastName varchar(50),
    trainCardID integer
);

INSERT INTO passengers
VALUES (1123, 'joe', 'smith', 1), (1342, 'mouse', 'cheese', 2), (1234, 'lily', 'lax', 3);

CREATE TABLE conductors (
    conductorID integer,
    firstName varchar(50),
    lastName varchar(50),
    mgrID integer, 
    startDate DATE
);

INSERT INTO conductors
VALUES (34, 'bob', 'bread', 1, '2018-01-01'), (13, 'a', 'b', 1, '2019-12-11'), (27, 'cedric', 'star', 3, '1999-04-28');

CREATE TABLE managers (
    managerID integer,
    firstName varchar(50),
    lastName varchar(50)
);

INSERT INTO managers
VALUES (1, 'mickey', 'mouse'), (2, 'donald', 'duck'), (3, 'goofy', 'ralph');

CREATE TABLE trainCard (
    cardID integer, 
    pID integer, 
    currentBalance integer
);

INSERT INTO trainCard
VALUES (456, 1123, 0), (65, 1342, 21), (78, 1234, 15);

CREATE TABLE transactions (
    transactionID integer, 
    transType varchar(40), 
    amount integer, 
    cID integer, 
    pID integer,
    transTimeStamp DATETIME
);

INSERT INTO transactions
VALUES (234, 'deposit', 10, 456, 1123, '2022-11-23 00:00:00'), (235, 'withdraw', 3, 456, 1123, '2022-11-23 00:00:00');

CREATE TABLE train (
    trainID integer, 
    passengerCapacity integer, 
    condID integer, 
    mgrID integer
);

INSERT INTO train
VALUES (2, 150, 34, 1), (15, 187, 23, 2), (16, 200, 9, 3);

CREATE TABLE feedback (
    feedbackID integer, 
    condID integer, 
    submitterID integer, 
    comment varchar(100), 
    trainID integer,
    rating integer, 
    fdbkTimeStamp DATETIME, 
    category text
);

INSERT INTO feedback
VALUES (1, 34, 1123, "train was slow to move", 2, 3, '2021-11-30 12:34:56', "late"), 
(2, 13, 154, "train didn't come on time", 15, 2, '2022-12-11 07:18:03', "late"),
(3, 13, 167, "where's the train?!?!?", 15, 1, '2021-12-11 07:11:01', "late"), 
(4, 27, 80, "more or less a good experience", 16, 4, '2021-12-08 15:15:20', "positive");

CREATE TABLE schedule (
    schID integer, 
    trainID integer, 
    routeID integer, 
    departureTime datetime,
    isDelayed boolean
);

INSERT INTO schedule
VALUES (1, 2, 3, '2022-11-24 11:00:00', false), (2, 15, 1, '2022-11-24 10:35:55', true);

CREATE TABLE delays (
    delayID integer, 
    schID integer, 
    trainID integer, 
    routeID integer,
    minLate integer
);

INSERT INTO delays
VALUES (1, 2, 15, 1, 5);

CREATE TABLE route (
    routeID integer, 
    routeName text, 
    origin integer, 
    destination integer, 
    routeLine text, 
    direction text
);

INSERT INTO route 
VALUES (1, 'bowdoin to wonderland', 01, 12, 'BL', 'west-bound');

CREATE TABLE stop (
    stopID integer, 
    stopName text
);

INSERT INTO stop 
VALUES (01, 'bowdoin'), (02, 'government center');

CREATE TABLE routeStops (
    rtID integer, 
    rsStopID integer, 
    duration integer
);

INSERT INTO routeStops 
VALUES (1, 01, 6), (1, 04, 8), (1, 05, 10);
