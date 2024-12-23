from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from flet.core.alignment import Alignment
from flet.core.border import Border
from flet.core.gradients import Gradient
from flet.core.types import (
    BlendMode,
    BorderRadiusValue,
    ColorValue,
    ImageFit,
    ImageRepeat,
    Number,
    OffsetValue,
    OptionalNumber,
)


@dataclass
class ColorFilter:
    color: Optional[ColorValue] = field(default=None)
    blend_mode: Optional[BlendMode] = field(default=None)


class FilterQuality(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ShadowBlurStyle(Enum):
    NORMAL = "normal"
    SOLID = "solid"
    OUTER = "outer"
    INNER = "inner"


@dataclass
class BoxShadow:
    spread_radius: Optional[float] = field(default=None)
    blur_radius: Optional[float] = field(default=None)
    color: Optional[ColorValue] = field(default=None)
    offset: OffsetValue = field(default=None)
    blur_style: ShadowBlurStyle = field(default=ShadowBlurStyle.NORMAL)


class BoxShape(Enum):
    RECTANGLE = "rectangle"
    CIRCLE = "circle"


@dataclass
class DecorationImage:
    src: Optional[str] = None
    src_base64: Optional[str] = None
    color_filter: Optional[ColorFilter] = None
    fit: Optional[ImageFit] = None
    alignment: Optional[Alignment] = None
    repeat: Optional[ImageRepeat] = None
    match_text_direction: Optional[bool] = None
    scale: OptionalNumber = None
    opacity: OptionalNumber = None
    filter_quality: Optional[FilterQuality] = None
    invert_colors: Optional[bool] = None
    anti_alias: Optional[bool] = None


@dataclass
class BoxDecoration:
    bgcolor: Optional[ColorValue] = None
    image: Optional[DecorationImage] = None
    border: Optional[Border] = None
    border_radius: BorderRadiusValue = None
    shadow: Union[None, BoxShadow, List[BoxShadow]] = None
    gradient: Optional[Gradient] = None
    shape: Optional[BoxShape] = None
    blend_mode: Optional[BlendMode] = None


@dataclass
class BoxConstraints:
    min_width: Number = 0
    min_height: Number = 0
    max_width: Number = float("inf")
    max_height: Number = float("inf")

    def __post_init__(self):
        assert (
            self.min_width <= self.max_width
        ), "min_width must be less than or equal to max_width"
        assert (
            self.min_height <= self.max_height
        ), "min_height must be less than or equal to max_height"
