import React from "react";
import AppShell from "../components/AppShell.jsx";
import StatCard from "../components/StatCard.jsx";
import { PageHeader } from "./SafetyIntelligence.jsx";

const workers = [{ name: "Site crew A", zone: "North elevation", status: "Monitored", risk: "Low" }, { name: "Site crew B", zone: "Concrete deck", status: "Review needed", risk: "Medium" }, { name: "Electrical team", zone: "Service corridor", status: "Monitored", risk: "Low" }];
function Workers() { return <AppShell><PageHeader title="Workers" description="Monitor workforce exposure and follow up on safety observations." /><div className="stats-grid compact"><StatCard label="Workers on site" value="185" detail="12 zones reporting" /><StatCard label="Monitored" value="176" detail="95% coverage" tone="green" /><StatCard label="Needs review" value="9" detail="Assigned today" tone="orange" /></div><section className="panel table-panel"><h2>Active teams</h2><div className="data-table">{workers.map((worker) => <div className="table-row" key={worker.name}><strong>{worker.name}</strong><span>{worker.zone}</span><span>{worker.status}</span><span className="status-pill">{worker.risk} risk</span></div>)}</div></section></AppShell>; }
export default Workers;
