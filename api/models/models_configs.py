from pydantic import ConfigDict

base_model_config = ConfigDict(
    populate_by_name=True,
    arbitrary_types_allowed=True,
    from_attributes=True,
)