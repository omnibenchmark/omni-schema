# Auto generated from omni_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-03-08T14:09:16
# Schema: omni-schema
#
# id: https://w3id.org/omnibenchmark/omni-schema
# description: Data model for omnibenchmark.
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OMNI_SCHEMA = CurieNamespace('omni_schema', 'https://w3id.org/omnibenchmark/omni-schema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OMNI_SCHEMA


# Types

# Class references
class IdentifiableEntityId(URIorCURIE):
    pass


class BenchmarkId(IdentifiableEntityId):
    pass


class StepId(IdentifiableEntityId):
    pass


class ModuleId(IdentifiableEntityId):
    pass


class IOFileId(IdentifiableEntityId):
    pass


@dataclass
class IdentifiableEntity(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "IdentifiableEntity"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.IdentifiableEntity

    id: Union[str, IdentifiableEntityId] = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifiableEntityId):
            self.id = IdentifiableEntityId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Benchmark(IdentifiableEntity):
    """
    A multi-step workflow to evaluate processing steps for a specific task.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Benchmark"]
    class_class_curie: ClassVar[str] = "omni_schema:Benchmark"
    class_name: ClassVar[str] = "Benchmark"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Benchmark

    id: Union[str, BenchmarkId] = None
    name: str = None
    version: str = None
    platform: str = None
    storage: str = None
    orchestrator: Union[dict, "Orchestrator"] = None
    validator: Union[dict, "Validator"] = None
    steps: Union[Dict[Union[str, StepId], Union[dict, "Step"]], List[Union[dict, "Step"]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BenchmarkId):
            self.id = BenchmarkId(self.id)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.platform):
            self.MissingRequiredField("platform")
        if not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self._is_empty(self.storage):
            self.MissingRequiredField("storage")
        if not isinstance(self.storage, str):
            self.storage = str(self.storage)

        if self._is_empty(self.orchestrator):
            self.MissingRequiredField("orchestrator")
        if not isinstance(self.orchestrator, Orchestrator):
            self.orchestrator = Orchestrator(**as_dict(self.orchestrator))

        if self._is_empty(self.validator):
            self.MissingRequiredField("validator")
        if not isinstance(self.validator, Validator):
            self.validator = Validator(**as_dict(self.validator))

        if self._is_empty(self.steps):
            self.MissingRequiredField("steps")
        self._normalize_inlined_as_list(slot_name="steps", slot_type=Step, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Orchestrator(YAMLRoot):
    """
    The orchestrator of the benchmark.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Orchestrator"]
    class_class_curie: ClassVar[str] = "omni_schema:Orchestrator"
    class_name: ClassVar[str] = "Orchestrator"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Orchestrator

    name: str = None
    url: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Validator(YAMLRoot):
    """
    The validator of the benchmark.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Validator"]
    class_class_curie: ClassVar[str] = "omni_schema:Validator"
    class_name: ClassVar[str] = "Validator"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Validator

    name: str = None
    url: str = None
    schema_url: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self._is_empty(self.schema_url):
            self.MissingRequiredField("schema_url")
        if not isinstance(self.schema_url, str):
            self.schema_url = str(self.schema_url)

        super().__post_init__(**kwargs)


@dataclass
class Step(IdentifiableEntity):
    """
    A benchmark subtask with equivalent and independent modules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Step"]
    class_class_curie: ClassVar[str] = "omni_schema:Step"
    class_name: ClassVar[str] = "Step"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Step

    id: Union[str, StepId] = None
    name: str = None
    members: Union[Dict[Union[str, ModuleId], Union[dict, "Module"]], List[Union[dict, "Module"]]] = empty_dict()
    initial: Optional[Union[bool, Bool]] = None
    terminal: Optional[Union[bool, Bool]] = None
    after: Optional[Union[Union[str, StepId], List[Union[str, StepId]]]] = empty_list()
    inputs: Optional[Union[Union[dict, "InputCollection"], List[Union[dict, "InputCollection"]]]] = empty_list()
    outputs: Optional[Union[Dict[Union[str, IOFileId], Union[dict, "IOFile"]], List[Union[dict, "IOFile"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StepId):
            self.id = StepId(self.id)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        self._normalize_inlined_as_list(slot_name="members", slot_type=Module, key_name="id", keyed=True)

        if self.initial is not None and not isinstance(self.initial, Bool):
            self.initial = Bool(self.initial)

        if self.terminal is not None and not isinstance(self.terminal, Bool):
            self.terminal = Bool(self.terminal)

        if not isinstance(self.after, list):
            self.after = [self.after] if self.after is not None else []
        self.after = [v if isinstance(v, StepId) else StepId(v) for v in self.after]

        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, InputCollection) else InputCollection(**as_dict(v)) for v in self.inputs]

        self._normalize_inlined_as_list(slot_name="outputs", slot_type=IOFile, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Module(IdentifiableEntity):
    """
    A single benchmark component assigned to a specific step.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Module"]
    class_class_curie: ClassVar[str] = "omni_schema:Module"
    class_name: ClassVar[str] = "Module"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Module

    id: Union[str, ModuleId] = None
    name: str = None
    repo: str = None
    exclude: Optional[Union[Union[str, ModuleId], List[Union[str, ModuleId]]]] = empty_list()
    parameters: Optional[Union[Union[dict, "Parameter"], List[Union[dict, "Parameter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModuleId):
            self.id = ModuleId(self.id)

        if self._is_empty(self.repo):
            self.MissingRequiredField("repo")
        if not isinstance(self.repo, str):
            self.repo = str(self.repo)

        if not isinstance(self.exclude, list):
            self.exclude = [self.exclude] if self.exclude is not None else []
        self.exclude = [v if isinstance(v, ModuleId) else ModuleId(v) for v in self.exclude]

        if not isinstance(self.parameters, list):
            self.parameters = [self.parameters] if self.parameters is not None else []
        self.parameters = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.parameters]

        super().__post_init__(**kwargs)


@dataclass
class IOFile(IdentifiableEntity):
    """
    Represents an input / output file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["IOFile"]
    class_class_curie: ClassVar[str] = "omni_schema:IOFile"
    class_name: ClassVar[str] = "IOFile"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.IOFile

    id: Union[str, IOFileId] = None
    name: str = None
    path: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IOFileId):
            self.id = IOFileId(self.id)

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        super().__post_init__(**kwargs)


@dataclass
class InputCollection(YAMLRoot):
    """
    A holder for valid input combinations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["InputCollection"]
    class_class_curie: ClassVar[str] = "omni_schema:InputCollection"
    class_name: ClassVar[str] = "InputCollection"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.InputCollection

    entries: Optional[Union[Union[str, IOFileId], List[Union[str, IOFileId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, IOFileId) else IOFileId(v) for v in self.entries]

        super().__post_init__(**kwargs)


@dataclass
class Parameter(YAMLRoot):
    """
    A parameter and its scope.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMNI_SCHEMA["Parameter"]
    class_class_curie: ClassVar[str] = "omni_schema:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = OMNI_SCHEMA.Parameter

    values: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, str) else str(v) for v in self.values]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=OMNI_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=OMNI_SCHEMA.name, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=OMNI_SCHEMA.description, domain=None, range=Optional[str])

slots.version = Slot(uri=OMNI_SCHEMA.version, name="version", curie=OMNI_SCHEMA.curie('version'),
                   model_uri=OMNI_SCHEMA.version, domain=None, range=str)

slots.platform = Slot(uri=OMNI_SCHEMA.platform, name="platform", curie=OMNI_SCHEMA.curie('platform'),
                   model_uri=OMNI_SCHEMA.platform, domain=None, range=str)

slots.storage = Slot(uri=OMNI_SCHEMA.storage, name="storage", curie=OMNI_SCHEMA.curie('storage'),
                   model_uri=OMNI_SCHEMA.storage, domain=None, range=str)

slots.orchestrator = Slot(uri=OMNI_SCHEMA.orchestrator, name="orchestrator", curie=OMNI_SCHEMA.curie('orchestrator'),
                   model_uri=OMNI_SCHEMA.orchestrator, domain=None, range=Union[dict, Orchestrator])

slots.validator = Slot(uri=OMNI_SCHEMA.validator, name="validator", curie=OMNI_SCHEMA.curie('validator'),
                   model_uri=OMNI_SCHEMA.validator, domain=None, range=Union[dict, Validator])

slots.steps = Slot(uri=OMNI_SCHEMA.steps, name="steps", curie=OMNI_SCHEMA.curie('steps'),
                   model_uri=OMNI_SCHEMA.steps, domain=None, range=Union[Dict[Union[str, StepId], Union[dict, Step]], List[Union[dict, Step]]])

slots.url = Slot(uri=OMNI_SCHEMA.url, name="url", curie=OMNI_SCHEMA.curie('url'),
                   model_uri=OMNI_SCHEMA.url, domain=None, range=str)

slots.schema_url = Slot(uri=OMNI_SCHEMA.schema_url, name="schema_url", curie=OMNI_SCHEMA.curie('schema_url'),
                   model_uri=OMNI_SCHEMA.schema_url, domain=None, range=str)

slots.initial = Slot(uri=OMNI_SCHEMA.initial, name="initial", curie=OMNI_SCHEMA.curie('initial'),
                   model_uri=OMNI_SCHEMA.initial, domain=None, range=Optional[Union[bool, Bool]])

slots.terminal = Slot(uri=OMNI_SCHEMA.terminal, name="terminal", curie=OMNI_SCHEMA.curie('terminal'),
                   model_uri=OMNI_SCHEMA.terminal, domain=None, range=Optional[Union[bool, Bool]])

slots.after = Slot(uri=OMNI_SCHEMA.after, name="after", curie=OMNI_SCHEMA.curie('after'),
                   model_uri=OMNI_SCHEMA.after, domain=None, range=Optional[Union[Union[str, StepId], List[Union[str, StepId]]]])

slots.members = Slot(uri=OMNI_SCHEMA.members, name="members", curie=OMNI_SCHEMA.curie('members'),
                   model_uri=OMNI_SCHEMA.members, domain=None, range=Union[Dict[Union[str, ModuleId], Union[dict, Module]], List[Union[dict, Module]]])

slots.inputs = Slot(uri=OMNI_SCHEMA.inputs, name="inputs", curie=OMNI_SCHEMA.curie('inputs'),
                   model_uri=OMNI_SCHEMA.inputs, domain=None, range=Optional[Union[Union[dict, InputCollection], List[Union[dict, InputCollection]]]])

slots.outputs = Slot(uri=OMNI_SCHEMA.outputs, name="outputs", curie=OMNI_SCHEMA.curie('outputs'),
                   model_uri=OMNI_SCHEMA.outputs, domain=None, range=Optional[Union[Dict[Union[str, IOFileId], Union[dict, IOFile]], List[Union[dict, IOFile]]]])

slots.exclude = Slot(uri=OMNI_SCHEMA.exclude, name="exclude", curie=OMNI_SCHEMA.curie('exclude'),
                   model_uri=OMNI_SCHEMA.exclude, domain=None, range=Optional[Union[Union[str, ModuleId], List[Union[str, ModuleId]]]])

slots.repo = Slot(uri=OMNI_SCHEMA.repo, name="repo", curie=OMNI_SCHEMA.curie('repo'),
                   model_uri=OMNI_SCHEMA.repo, domain=None, range=str)

slots.parameters = Slot(uri=OMNI_SCHEMA.parameters, name="parameters", curie=OMNI_SCHEMA.curie('parameters'),
                   model_uri=OMNI_SCHEMA.parameters, domain=None, range=Optional[Union[Union[dict, Parameter], List[Union[dict, Parameter]]]])

slots.path = Slot(uri=OMNI_SCHEMA.path, name="path", curie=OMNI_SCHEMA.curie('path'),
                   model_uri=OMNI_SCHEMA.path, domain=None, range=Optional[str])

slots.values = Slot(uri=OMNI_SCHEMA.values, name="values", curie=OMNI_SCHEMA.curie('values'),
                   model_uri=OMNI_SCHEMA.values, domain=None, range=Optional[Union[str, List[str]]])

slots.entries = Slot(uri=OMNI_SCHEMA.entries, name="entries", curie=OMNI_SCHEMA.curie('entries'),
                   model_uri=OMNI_SCHEMA.entries, domain=None, range=Optional[Union[Union[str, IOFileId], List[Union[str, IOFileId]]]])