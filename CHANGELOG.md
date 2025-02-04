# Change Log

This document records all notable changes to `omni-schema`.
This project adheres to [Semantic Versioning](https://semver.org/).

## 0.0.5 UNRELEASED
- Added:
    - `metric_collectors` field to Benchmark

## [0.0.4](https://github.com/omnibenchmark/omni-schema/releases/tag/version%2F0.0.4) 
- Added:
    - `storage_bucket_name` field


## [0.0.3](https://github.com/omnibenchmark/omni-schema/releases/tag/version%2F0.0.3) 
- Added:
    - `software_backend` field


## [0.0.2](https://github.com/omnibenchmark/omni-schema/releases/tag/version%2F0.0.2) 
- Removed:
    - `orchestrator`, `validator`, `platform` fields
- Added:
    - `storage_api`, `software_environments`, `benchmark_yaml_spec` fields
- Changes:
    - rename `repo` to `repository`
    - rename `steps` to `stages`
    - rename `members` to `modules`
    - add `commit` and `url` field to Repository model


## [0.0.1](https://github.com/omnibenchmark/omni-schema/releases/tag/version%2F0.0.1) 
Initial omni-schema release.