from typing import Annotated

from pydantic import Field

PhoneNumber = Annotated[str, Field(pattern=r"^\+380\d{9}$")]
