

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	PRIMARY KEY (id)
);

CREATE TABLE "BenchmarkCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
