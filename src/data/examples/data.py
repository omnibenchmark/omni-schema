from omni_schema.datamodel.omni_schema import *

Benchmark_001 = Benchmark(
    id=BenchmarkId('Benchmark_001'),
    name='starts_to_be_explicit',
    description='simple benchmark, somewhat explicit, simple params',
    version='1.0',
    platform='https://github.com/',
    storage='https://storage.github.com/',
    orchestrator=Orchestrator(
        name='orchestrator',
        url='https://github.com/omnibenchmark/test/orchestrator',
    ),
    validator=Validator(
        name='validator',
        url='https://github.com/omnibenchmark/test/validator',
        schema_url='https://github.com/omnibenchmark/omni_essentials'
    ),
    steps=[
        Step(
            id=StepId('Step1'),
            name='data',
            initial=True,
            members=[
                Module(
                    id=ModuleId('D1'),
                    name='D1',
                    repo='omnibenchmark/test/D1'
                ),
                Module(
                    id=ModuleId('D2'),
                    name='D2',
                    repo='omnibenchmark/test/D2'
                )
            ],
            outputs=[
                IOFile(
                    id=IOFileId('Step1.counts'),
                    name='counts',
                    path='{stage}/{module}/{params}/{name}.txt.gz'
                ),
                IOFile(
                    id=IOFileId('Step1.meta'),
                    name='meta',
                    path='{stage}/{module}/{params}/{name}.meta.json'
                ),
                IOFile(
                    id=IOFileId('Step1.data_specific_params'),
                    name='data_specific_params',
                    path='{stage}/{module}/{params}/{name}_params.txt'
                )
            ]
        ),
        Step(
            id='Step2',
            name='process',
            members=[
                Module(
                    id='P1',
                    name='P1',
                    repo='omnibenchmark/test/P1',
                    parameters=[
                        Parameter(values=['-a 0', '-b 0.1']),
                        Parameter(values=['-a 1', '-b 0.1'])
                    ]),
                Module(
                    id='P2',
                    name='P2',
                    repo='omnibenchmark/test/P2',
                    parameters=[
                        Parameter(values=['-a 0', '-c 0']),
                        Parameter(values=['-a 1', '-c 0.1'])
                    ]
                )
            ],
            after=['data'],
            inputs=[
                InputCollection(
                    entries=['Step1.counts', 'Step1.meta']
                )
            ],
            outputs=[
                IOFile(
                    id='Step2.filtered',
                    name='filtered',
                    path='{input_dirname}/{stage}/{module}/{params}/{name}.txt.gz'
                )
            ]
        ),
        Step(
            id='Step3',
            name='methods',
            members=[
                Module(
                    id='M1',
                    name='M1',
                    repo='benchmark/test/M1',
                    exclude=['D2']
                ),
                Module(
                    id='M2',
                    name='M2',
                    repo='omnibenchmark/test/M2',
                    exclude=['D1', 'D2'],
                    parameters=[
                        Parameter(values=['-d1', '-e 1']),
                        Parameter(values=['-d1', '-e 2'])
                    ]
                )
            ],
            after=['process'],
            inputs=[
                InputCollection(
                    entries=['Step1.counts', 'Step1.meta', 'Step1.data_specific_params']
                ),
                InputCollection(
                    entries=['Step2.filtered', 'Step1.meta', 'Step1.data_specific_params']
                )
            ],
            outputs=[
                IOFile(
                    id='Step3.mapping',
                    name='mapping',
                    path='{input_dirname}/{stage}/{module}/{params}/{name}.model.out.gz'
                )
            ]
        ),
        Step(
            id='Step4',
            name='metrics',
            members=[
                Module(
                    id='m1',
                    name='m1',
                    repo='omnibenchmark/test/m1'
                ),
                Module(
                    id='m2',
                    name='m2',
                    repo='omnibenchmark/test/m2'
                ),
                Module(
                    id='m3',
                    name='m3',
                    repo='omnibenchmark/test/m3'
                )
            ],
            terminal=True,
            after=['methods'],
            inputs=[
                InputCollection(
                    entries=['Step3.mapping', 'Step1.meta', 'Step1.data_specific_params']
                )
            ]
        )
    ]
)