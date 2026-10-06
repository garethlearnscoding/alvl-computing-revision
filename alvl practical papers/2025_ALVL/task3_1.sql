CREATE TABLE "User" (
	"Username"	TEXT,
	"Blocked"	INTEGER,
	PRIMARY KEY("Username")
);

CREATE TABLE "Post" (
	"PostID"	INTEGER,
	"PostText"	TEXT,
	"DateTimePosted"	TEXT,
	"Username"	TEXT,
	FOREIGN KEY("Username") REFERENCES "User"("Username"),
	PRIMARY KEY("PostID")
);

CREATE TABLE "Comment" (
	"CommentID"	INTEGER,
	"PostID"	TEXT,
	"Username"	TEXT,
	"TheText"	TEXT,
	"DateTimeCommented"	TEXT,
	PRIMARY KEY("CommentID"),
	FOREIGN KEY("PostID") REFERENCES "Post"("PostID"),
	FOREIGN KEY("Username") REFERENCES "User"("Username")
);