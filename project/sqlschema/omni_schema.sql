

CREATE TABLE "Benchmark" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	version TEXT NOT NULL, 
	benchmarker TEXT NOT NULL, 
	software_backend TEXT NOT NULL, 
	storage TEXT NOT NULL, 
	storage_api VARCHAR(2) NOT NULL, 
	software_environments TEXT NOT NULL, 
	benchmark_yaml_spec TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "IOFile" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	path TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Repository" (
	url TEXT NOT NULL, 
	"commit" TEXT NOT NULL, 
	PRIMARY KEY (url, "commit")
);

CREATE TABLE "SoftwareEnvironment" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	easyconfig TEXT, 
	envmodule TEXT, 
	conda TEXT, 
	apptainer TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Module" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	software_environment TEXT NOT NULL, 
	repository TEXT NOT NULL, 
	exclude TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(software_environment) REFERENCES "SoftwareEnvironment" (id)
);

CREATE TABLE "Stage" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	modules TEXT NOT NULL, 
	outputs TEXT, 
	"Benchmark_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Benchmark_id") REFERENCES "Benchmark" (id)
);

CREATE TABLE "InputCollection" (
	entries TEXT, 
	"Stage_id" TEXT, 
	PRIMARY KEY (entries, "Stage_id"), 
	FOREIGN KEY("Stage_id") REFERENCES "Stage" (id)
);

CREATE TABLE "Parameter" (
	"values" TEXT, 
	"Module_id" TEXT, 
	PRIMARY KEY ("values", "Module_id"), 
	FOREIGN KEY("Module_id") REFERENCES "Module" (id)
);
