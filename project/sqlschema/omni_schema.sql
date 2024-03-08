

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	version TEXT NOT NULL, 
	platform TEXT NOT NULL, 
	storage TEXT NOT NULL, 
	orchestrator TEXT NOT NULL, 
	validator TEXT NOT NULL, 
	steps TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "IOFile" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	path TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Module" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	repo TEXT NOT NULL, 
	exclude TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Orchestrator" (
	name TEXT NOT NULL, 
	url TEXT NOT NULL, 
	PRIMARY KEY (name, url)
);

CREATE TABLE "Step" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	initial BOOLEAN, 
	terminal BOOLEAN, 
	"after" TEXT, 
	members TEXT NOT NULL, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Validator" (
	name TEXT NOT NULL, 
	url TEXT NOT NULL, 
	schema_url TEXT NOT NULL, 
	PRIMARY KEY (name, url, schema_url)
);

CREATE TABLE "InputCollection" (
	entries TEXT, 
	"Step_id" TEXT, 
	PRIMARY KEY (entries, "Step_id"), 
	FOREIGN KEY("Step_id") REFERENCES "Step" (id)
);

CREATE TABLE "Parameter" (
	"values" TEXT, 
	"Module_id" TEXT, 
	PRIMARY KEY ("values", "Module_id"), 
	FOREIGN KEY("Module_id") REFERENCES "Module" (id)
);
