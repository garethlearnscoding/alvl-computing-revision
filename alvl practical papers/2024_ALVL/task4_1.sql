CREATE TABLE `Villa` (
	`VillaID`	TEXT,
	`VillaName`	TEXT,
	`Country`	TEXT,
	`Cost`	NUMERIC,
	PRIMARY KEY(`VillaID`)
);

CREATE TABLE `CustomerBooking` (
	`BookingID`	TEXT,
	`CustomerID`	TEXT,
	`VillaID`	TEXT,
	`StartTime`	INTEGER,
	`NumberOfDays`	INTEGER,
	PRIMARY KEY(`BookingID`),
	FOREIGN KEY(`VillaID`) REFERENCES `Villa`(`VillaID`)
);