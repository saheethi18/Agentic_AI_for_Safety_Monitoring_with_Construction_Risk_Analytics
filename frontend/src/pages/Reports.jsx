import React from "react";
import AppShell from "../components/AppShell.jsx";
import { PageHeader } from "./SafetyIntelligence.jsx";

function Reports() { return <AppShell><PageHeader title="Reports" description="Prepare clear safety briefings for site and management teams." /><section className="panel report-panel"><div><span className="eyebrow">Weekly safety brief</span><h2>Construction risk summary</h2><p>Includes risk score, open alerts, PPE compliance, and corrective-action status for the active project.</p></div><button className="primary-button" onClick={() => window.print()}>Print report</button></section><section className="panel"><h2>Recent reports</h2><div className="data-table"><div className="table-row"><strong>Week 35 safety brief</strong><span>Generated today</span><span>PDF</span><button className="text-button" onClick={() => window.print()}>Open</button></div><div className="table-row"><strong>Monthly management review</strong><span>31 Aug 2026</span><span>PDF</span><button className="text-button" onClick={() => window.print()}>Open</button></div></div></section></AppShell>; }
export default Reports;
