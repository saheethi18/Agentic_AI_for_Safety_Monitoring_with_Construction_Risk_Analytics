from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.dataset import router as dataset_router

app = FastAPI(
    title="BuildSure AI",
    description="Construction Site Risk Monitoring API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(dataset_router)

@app.get("/")
def root():
    return {
        "message": "BuildSure AI Backend is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "BuildSure AI Backend"
    }

@app.get("/site-risk/{project_id}")
def get_site_risk(project_id: str):
    """Quick site risk response without heavy processing"""
    valid_projects = ["P001", "P002", "P003"]
    
    if project_id not in valid_projects:
        return {"error": "Project not found"}, 404
    
    return {
        "projectId": project_id,
        "projectName": "ABC Construction Project",
        "location": "Hyderabad",
        "riskScore": 65,
        "riskLevel": "HIGH",
        "monitoring": {
            "workers": 185,
            "equipment": 24,
            "temperature": 39.0,
            "humidity": 72.0,
            "previousIncidents": 4
        },
        "riskFactors": {
            "environmental": 75.0,
            "equipment": 65.0,
            "workerExposure": 80.0,
            "incidentHistory": 70.0
        },
        "hazards": [
            {
                "id": 1,
                "name": "Missing Hardhat",
                "confidence": 0.92,
                "location": "Section A",
                "severity": "HIGH"
            }
        ],
        "recommendations": [
            "Ensure all workers wear proper PPE",
            "Increase site monitoring frequency"
        ]
    }