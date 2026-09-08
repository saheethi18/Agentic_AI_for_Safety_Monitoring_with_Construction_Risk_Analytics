import React from "react";
import AppShell from "../components/AppShell.jsx";
import AlertCard from "../components/AlertCard.jsx";
import { PageHeader } from "./SafetyIntelligence.jsx";

const alerts = [{ title: "Missing eye protection", description: "Three workers were observed in the cutting zone without eye protection.", severity: "high", time: "12 min ago" }, { title: "Vehicle proximity", description: "A pedestrian entered the active equipment exclusion zone.", severity: "critical", time: "28 min ago" }, { title: "Heat exposure rising", description: "Temperature and humidity crossed the site monitoring threshold.", severity: "medium", time: "1 hr ago" }];
function Alerts() { return <AppShell><PageHeader title="Alerts" description="Review open observations and assign corrective actions." /><div className="alert-list">{alerts.map((alert) => <AlertCard key={alert.title} alert={alert} />)}</div></AppShell>; }
export default Alerts;
