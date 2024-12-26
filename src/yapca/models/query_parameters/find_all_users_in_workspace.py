from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserStatus(str, Enum):
    """Enum for possible user statuses."""

    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    DECLINED = "DECLINED"
    INACTIVE = "INACTIVE"
    ALL = "ALL"


class AccountStatus(str, Enum):
    """Enum for account statuses."""

    LIMITED = "LIMITED"  # Additional statuses can be added here as necessary
    ACTIVE = "ACTIVE"
    PENDING_EMAIL_VERIFICATION = "PENDING_EMAIL_VERIFICATION"
    NOT_REGISTERED = "NOT_REGISTERED"


class SortColumn(str, Enum):
    """Enum for sort-column criteria."""

    ID = "ID"
    EMAIL = "EMAIL"
    NAME = "NAME"
    NAME_LOWERCASE = "NAME_LOWERCASE"
    ACCESS = "ACCESS"
    HOURLYRATE = "HOURLYRATE"
    COSTRATE = "COSTRATE"


class SortOrder(str, Enum):
    """Enum for sort-order modes."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class Memberships(str, Enum):
    """Enum for membership types."""

    ALL = "ALL"
    NONE = "NONE"
    WORKSPACE = "WORKSPACE"
    PROJECT = "PROJECT"
    USERGROUP = "USERGROUP"


class GetUsersQueryParams(BaseModel):
    """
    Query parameters for the getUsersOfWorkspace API endpoint.
    """

    email: Optional[EmailStr] = None
    project_id: Optional[str] = None
    status: Optional[UserStatus] = UserStatus.ALL
    account_statuses: Optional[AccountStatus] = None
    name: Optional[str] = None
    sort_column: Optional[SortColumn] = SortColumn.EMAIL
    sort_order: Optional[SortOrder] = SortOrder.ASCENDING
    page: Optional[str] = "1"
    page_size: Optional[str] = "50"
    memberships: Optional[Memberships] = Memberships.NONE
    include_roles: bool = False

    def to_snake_case(s: str) -> str:
        return s.replace("-", "_")

    model_config = ConfigDict(alias_generator=to_snake_case, populate_by_name=True)
