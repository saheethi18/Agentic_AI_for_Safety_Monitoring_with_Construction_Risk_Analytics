from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class Project(BaseModel):
    id: str = "P001"
    name: str = "ABC Construction Project"
    location: str = "Hyderabad"


class MonitoringData(BaseModel):
    workers: int = 0
    equipment: int = 0
    temperature: float = 0.0
    humidity: float = 0.0
    previousIncidents: int = 0


class RiskFactors(BaseModel):
    environmental: float = 0.0
    equipment: float = 0.0
    workerExposure: float = 0.0
    incidentHistory: float = 0.0


class Hazard(BaseModel):
    id: int
    name: str
    category: str
    severity: str
    zone: str
    description: Optional[str] = ""
    status: str = "Detected"


class Recommendation(BaseModel):
    id: int
    message: str
    priority: str = "MEDIUM"
    category: Optional[str] = "Safety"


class SiteRiskInput(BaseModel):
    projectId: Optional[str] = "P001"
    projectName: Optional[str] = "ABC Construction Project"
    location: Optional[str] = "Hyderabad"

    workers: int = 185
    equipment: int = 24
    temperature: float = 39.0
    humidity: float = 72.0
    previousIncidents: int = 4

    environmentalRisk: float = 75.0
    equipmentRisk: float = 65.0
    workerExposure: float = 80.0
    incidentHistory: float = 70.0


class SiteRiskResponse(BaseModel):
    projectId: str
    projectName: str
    location: str
    riskScore: int
    riskLevel: str
    monitoring: MonitoringData
    riskFactors: RiskFactors
    hazards: List[Hazard]
    recommendations: List[Any]


class RiskScoreResponse(BaseModel):
    riskScore: int
    riskLevel: str
    message: str
    contributions: Dict[str, float]
    topRiskFactors: List[Dict[str, Any]]


class HazardResponse(BaseModel):
    projectId: str
    hazards: List[Hazard]
    totalHazards: int


class ProjectResponse(BaseModel):
    projects: List[Project]


class HealthResponse(BaseModel):
    status: str
    service: str = "BuildSure AI Backend"


class DatasetInfo(BaseModel):
    name: str
    category: str
    rows: int
    columns: List[str]


class ProcessedSiteData(BaseModel):
    workers: int
    equipment: int
    temperature: float
    humidity: float
    previousIncidents: int
    environmentalRisk: float
    equipmentRisk: float
    workerExposure: float
    incidentHistory: float