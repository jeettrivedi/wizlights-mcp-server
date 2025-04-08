from pydantic import BaseModel, Field, field_validator
from typing import Optional, Tuple


class StateModel(BaseModel):
    rgb: Optional[Tuple[float, float, float]] = Field(
        None,
        description="RGB values must be a tuple of three floats between 0 and 255.",
    )
    rgbw: Optional[Tuple[int, int, int, int]] = Field(
        None,
        description="RGBW values must be a tuple of four integers between 0 and 255.",
    )
    rgbww: Optional[Tuple[int, int, int, int, int]] = Field(
        None,
        description="RGBWW values must be a tuple of five integers between 0 and 255.",
    )

    @classmethod
    def validate_tuple(cls, values: Optional[Tuple], length: int, field_name: str):
        if values is not None:
            if len(values) != length:
                raise ValueError(f"{field_name} must have exactly {length} elements.")
            if not all(0 <= v <= 255 for v in values):
                raise ValueError(
                    f"All values in {field_name} must be between 0 and 255."
                )
        return values

    @field_validator("rgb")
    def validate_rgb(cls, value):
        return cls.validate_tuple(value, 3, "RGB")

    @field_validator("rgbw")
    def validate_rgbw(cls, value):
        return cls.validate_tuple(value, 4, "RGBW")

    @field_validator("rgbww")
    def validate_rgbww(cls, value):
        return cls.validate_tuple(value, 5, "RGBWW")

    brightness: Optional[int] = Field(
        None, ge=0, le=255, description="Brightness must be between 0 and 255."
    )
    colortemp: Optional[int] = Field(
        None,
        ge=2000,
        le=6500,
        description="Color temperature must be between 2000 and 6500.",
    )
    warm_white: Optional[int] = Field(
        None, ge=0, le=255, description="Warm white must be between 0 and 255."
    )
    cold_white: Optional[int] = Field(
        None, ge=0, le=255, description="Cold white must be between 0 and 255."
    )
    speed: Optional[int] = Field(
        None, ge=0, le=100, description="Speed must be between 0 and 100."
    )
    scene: Optional[int] = Field(None, description="Scene must be an integer.")
    hucolor: Optional[Tuple[float, float]] = Field(
        None, description="Hue color must be a tuple of two floats."
    )
    ratio: Optional[int] = Field(
        None, ge=0, le=100, description="Ratio must be between 0 and 100."
    )
    state: Optional[bool] = Field(True, description="State must be a boolean value.")
