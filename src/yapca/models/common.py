from pydantic import BaseModel


class CostRate(BaseModel):
    amount: int
    currency: str


class Currency(BaseModel):
    code: str
    id: str
    isDefault: bool


class HourlyRate(BaseModel):
    amount: int
    currency: str


class Membership(BaseModel):
    costRate: CostRate | None
    hourlyRate: HourlyRate | None
    membershipStatus: str
    membershipType: str
    targetId: str
    userId: str
