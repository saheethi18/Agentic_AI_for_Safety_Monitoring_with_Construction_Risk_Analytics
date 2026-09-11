import React from "react";
import AppShell from "../components/AppShell.jsx";
import StatCard from "../components/StatCard.jsx";
import { PageHeader } from "./SafetyIntelligence.jsx";

function Analytics() { return <AppShell><PageHeader title="Analytics" description="See how risk, compliance, and corrective actions trend over time." /><div className="stats-grid compact"><StatCard label="Average risk score" value="64" detail="Down 8% from last week" tone="orange" /><StatCard label="Open actions" value="23" detail="7 due today" tone="blue" /><StatCard label="Resolved this month" value="91" detail="14% faster than last month" tone="green" /></div><section className="panel chart-panel"><div className="panel-heading"><h2>Risk trend</h2><span className="status-pill">Last 14 days</span></div><div className="bar-chart" aria-label="Risk scores over the last seven days">{[42, 55, 48, 71, 64, 58, 36].map((height, index) => <span key={index} style={{ height: `${height}%` }} />)}</div></section></AppShell>; }
export default Analytics;
