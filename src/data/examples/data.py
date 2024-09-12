from src.omni_schema.datamodel.omni_schema import *

Benchmark_001 = Benchmark(
    id=BenchmarkId('Benchmark_001'),
    description='simple benchmark, somewhat explicit, simple params',
    version='1.0',
    benchmarker='John Doe at Robinsons lab, john.doe@uzh.ch',
    storage='https://storage.github.com/',
    storage_api=StorageAPIEnum.S3,
    storage_bucket_name="benchmark001",
    software_backend=SoftwareBackendEnum.envmodules,
    software_environments=[
        SoftwareEnvironment(
            id=SoftwareEnvironmentId('R'),
            description="R 4.3.3 with gfbf-2023 toolchain",
            easyconfig='R_4.3.3-gfbf-2023b.eb',
            envmodule='R/4.3.3-gfbf-2023b',
            conda='R_4.3.3_try.yaml',
            apptainer='http://registry.ch/R_4.3.3-gfbf-2023b.sif'
        ),
        SoftwareEnvironment(
            id=SoftwareEnvironmentId('python'),
            description="Ppython3.12.0 with gfbf-2023 toolchain",
            easyconfig='python_vX-gfbf-2023b.eb',
            envmodule='python/vX-gfbf-2023b',
            conda='python_vX_test.yaml',
            apptainer='http://registry.ch/python_vX-gfbf-2023b.sif'
        )
    ],
    benchmark_yaml_spec='0.01',
    stages=[
        Stage(
            id=StageId('data'),
            modules=[
                Module(
                    id=ModuleId('D1'),
                    name='Dataset 1',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='https://github.com/omnibenchmark-example/data.git',
                        commit='061a981'
                    )
                ),
                Module(
                    id=ModuleId('D2'),
                    name='Dataset 2',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='https://github.com/omnibenchmark-example/data.git',
                        commit='061a981'
                    )
                )
            ],
            outputs=[
                IOFile(
                    id=IOFileId('data.counts'),
                    path='{in}/{stage}/{module}/{params}/{dataset}.txt.gz'
                ),
                IOFile(
                    id=IOFileId('data.meta'),
                    path='{in}/{stage}/{module}/{params}/{dataset}.meta.json'
                ),
                IOFile(
                    id=IOFileId('data.data_specific_params'),
                    path='{in}/{stage}/{module}/{params}/{dataset}_params.txt'
                )
            ]
        ),
        Stage(
            id='process',
            modules=[
                Module(
                    id='P1',
                    software_environment=SoftwareEnvironmentId('R'),
                    parameters=[
                        Parameter(values=['-a 0', '-b 0.1']),
                        Parameter(values=['-a 1', '-b 0.1'])
                    ],
                    repository=Repository(
                        url='https://github.com/omnibenchmark-example/process.git',
                        commit='24579a8'
                    )
                ),
                Module(
                    id='P2',
                    software_environment='R',
                    parameters=[
                        Parameter(values=['-a 0', '-c 0']),
                        Parameter(values=['-a 1', '-c 0.1'])
                    ],
                    repository=Repository(
                        url='https://github.com/omnibenchmark-example/process.git',
                        commit='24579a8'
                    )
                )
            ],
            inputs=[
                InputCollection(
                    entries=['data.counts', 'data.meta']
                )
            ],
            outputs=[
                IOFile(
                    id='process.filtered',
                    path='{in}/{stage}/{module}/{params}/{dataset}.txt.gz'
                )
            ]
        ),
        Stage(
            id='methods',
            modules=[
                Module(
                    id='M1',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                      url='https://github.com/omnibenchmark-example/method.git',
                      commit='709e114'
                    ),
                    exclude=['D2']
                ),
                Module(
                    id='M2',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='https://github.com/omnibenchmark-example/method.git',
                        commit='709e114'
                    ),
                    exclude=['D1'],
                    parameters=[
                        Parameter(values=['-d1', '-e 1']),
                        Parameter(values=['-d1', '-e 2'])
                    ]
                )
            ],
            inputs=[
                InputCollection(
                    entries=['data.counts', 'data.meta', 'data.data_specific_params']
                ),
                InputCollection(
                    entries=['process.filtered', 'data.meta', 'data.data_specific_params']
                )
            ],
            outputs=[
                IOFile(
                    id='methods.mapping',
                    path='{in}/{stage}/{module}/{params}/{dataset}.model.out.gz'
                )
            ]
        ),
        Stage(
            id='metrics',
            modules=[
                Module(
                    id='m1',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='git@github.com:omnibenchmark-example/metric.git',
                        commit='ba781d7'
                    )
                ),
                Module(
                    id='m2',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='git@github.com:omnibenchmark-example/metric.git',
                        commit='ba781d7'
                    )
                ),
                Module(
                    id='m3',
                    software_environment=SoftwareEnvironmentId('python'),
                    repository=Repository(
                        url='git@github.com:omnibenchmark-example/metric.git',
                        commit='ba781d7'
                    )
                )
            ],
            inputs=[
                InputCollection(
                    entries=['methods.mapping', 'data.meta', 'data.data_specific_params']
                )
            ],
            outputs=[
                IOFile(
                    id='metrics.mapping',
                    path='{in}/{stage}/{module}/{params}/{dataset}.results.txt'
                )
            ]
        )
    ]
)
