# generated by datamodel-codegen:
#   filename:  get_all_workspaces.json
#   timestamp: 2024-12-15T22:18:51+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, RootModel

from yapca.models.common import CostRate, Currency, HourlyRate, Membership


class Subdomain(BaseModel):
    enabled: bool
    name: str | None


class AutomaticLock(BaseModel):
    changeDay: str
    dayOfMonth: int
    firstDay: str
    olderThanPeriod: str
    olderThanValue: int
    type: str


class Round(BaseModel):
    minutes: str
    round: str


class WorkspaceSettings(BaseModel):
    adminOnlyPages: List[str]
    automaticLock: AutomaticLock | None
    canSeeTimeSheet: bool
    canSeeTracker: bool
    currencyFormat: str
    defaultBillableProjects: bool
    durationFormat: str
    forceDescription: bool
    forceProjects: bool
    forceTags: bool
    forceTasks: bool
    isProjectPublicByDefault: bool
    lockTimeEntries: str | None
    lockTimeZone: str | None
    multiFactorEnabled: bool
    numberFormat: str
    onlyAdminsCreateProject: bool
    onlyAdminsCreateTag: bool
    onlyAdminsCreateTask: bool
    onlyAdminsSeeAllTimeEntries: bool
    onlyAdminsSeeBillableRates: bool
    onlyAdminsSeeDashboard: bool
    onlyAdminsSeePublicProjectsEntries: bool
    projectFavorites: bool
    projectGroupingLabel: str
    projectPickerSpecialFilter: bool
    round: Round
    timeRoundingInReports: bool
    timeTrackingMode: str
    trackTimeDownToSecond: bool


class Workspace(BaseModel):
    costRate: CostRate
    currencies: List[Currency]
    featureSubscriptionType: str
    features: List[str]
    hourlyRate: HourlyRate
    id: str
    imageUrl: str
    memberships: List[Membership]
    name: str
    subdomain: Subdomain
    workspaceSettings: WorkspaceSettings


class Workspaces(RootModel[List[Workspace]]):
    root: List[Workspace]
