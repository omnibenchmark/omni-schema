

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	platform TEXT NOT NULL, 
	orchestrator TEXT NOT NULL, 
	steps TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "IOFile" (
	name TEXT, 
	path TEXT, 
	PRIMARY KEY (name, path)
);

CREATE TABLE "Module" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	repo TEXT NOT NULL, 
	exclude TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Orchestrator" (
	name TEXT, 
	url TEXT NOT NULL, 
	PRIMARY KEY (name, url)
);

CREATE TABLE "Step" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	initial BOOLEAN, 
	terminal BOOLEAN, 
	"after" TEXT, 
	members TEXT NOT NULL, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "InputCollection" (
	entries TEXT, 
	"Step_id" TEXT, 
	PRIMARY KEY (entries, "Step_id"), 
	FOREIGN KEY("Step_id") REFERENCES "Step" (id)
);

CREATE TABLE "Parameter" (
	name TEXT, 
	"Module_id" TEXT, 
	PRIMARY KEY (name, "Module_id"), 
	FOREIGN KEY("Module_id") REFERENCES "Module" (id)
);
