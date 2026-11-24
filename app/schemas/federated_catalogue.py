from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema

# The supplied Federated Catalogue OpenAPI declares @id, dcat:dataset, and
# dspace:participantId as arrays of strings. Its DatasetFilters example puts
# objects inside dcat:dataset, and the POST /datasets 200 example uses an
# object there as well. Those examples are kept on the schema for traceability
# and do not validate against the declared property types.


_DATASET_FILTERS_EXAMPLE = {
    "@context": {
        "@vocab": "https://w3id.org/edc/v0.0.1/ns/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "dspace": "https://w3id.org/dspace/v0.8/",
    },
    "@id": [],
    "dcat:dataset": [
        {"http://www.w3.org/ns/msc_dms#description": "Dataset 2 for Internal Processes from ttl file"},
        "http://www.w3.org/ns/msc_dms#aboutProcess",
        "http://www.w3.org/ns/msc_dms#relatedSpatialRegion",
        "http://www.w3.org/ns/msc_dms#name",
        {"odrl:hasPolicy": ["odrl:obligation"]},
    ],
    "dspace:participantId": [],
}


def _string_array_property(schema: dict[str, Any], description: str) -> None:
    """Drop the null branch Pydantic adds for an optional field."""
    any_of = schema.get("anyOf")
    if not isinstance(any_of, list):
        schema["description"] = description
        return
    arrays = [item for item in any_of if item.get("type") == "array"]
    if len(arrays) != 1:
        schema["description"] = description
        return
    title = schema.get("title")
    schema.clear()
    schema.update(arrays[0])
    schema["description"] = description
    if title:
        schema["title"] = title


class DatasetFilters(BaseModel):
    """Filters to narrow down the datasets.

    A JSON object where each key is a metadata property and each value holds
    the values to match. Send an empty object (or no body) to get all datasets.
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        json_schema_extra={"examples": [_DATASET_FILTERS_EXAMPLE]},
    )

    dataset_ids: list[str] | None = Field(
        default=None,
        alias="@id",
        description="Dataset identifiers to match.",
    )
    dataset_properties: list[str] | None = Field(
        default=None,
        alias="dcat:dataset",
        description="Metadata properties the dataset must contain.",
    )
    participant_ids: list[str] | None = Field(
        default=None,
        alias="dspace:participantId",
        description="Participant identifiers to match.",
    )

    @field_validator("dataset_ids", "dataset_properties", "participant_ids", mode="before")
    @classmethod
    def reject_null_declared_fields(cls, value: Any) -> Any:
        if value is None:
            raise ValueError("null is not an accepted value")
        return value

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        properties = json_schema.get("properties", {})
        _string_array_property(properties.get("@id", {}), "Dataset identifiers to match.")
        _string_array_property(properties.get("dcat:dataset", {}), "Metadata properties the dataset must contain.")
        _string_array_property(
            properties.get("dspace:participantId", {}),
            "Participant identifiers to match.",
        )
        json_schema["additionalProperties"] = {
            "anyOf": [
                {"items": {}, "type": "array"},
                {"additionalProperties": True, "type": "object"},
                {"type": "string"},
            ]
        }
        return json_schema

    @model_validator(mode="after")
    def validate_additional_properties(self) -> "DatasetFilters":
        extra = self.__pydantic_extra__ or {}
        for key, value in extra.items():
            if isinstance(value, (list, dict, str)):
                continue
            raise ValueError(f"Additional property '{key}' must be an array, object, or string.")
        return self


class FederatedCatalogueResponse(BaseModel):
    source_component: str = "IC4 Federated Catalogue"
    source_status: str
    data: Any | None = None
