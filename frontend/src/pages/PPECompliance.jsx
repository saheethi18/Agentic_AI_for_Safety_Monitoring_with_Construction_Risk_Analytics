import React from "react";
import AppShell from "../components/AppShell.jsx";
import PPEStatus from "../components/PPEStatus.jsx";
import { PageHeader } from "./SafetyIntelligence.jsx";

function PPECompliance() { return <AppShell><PageHeader title="PPE Compliance" description="Track whether required protective equipment is present and used." /><section className="panel"><div className="panel-heading"><div><span className="eyebrow">Live inspection</span><h2>Equipment readiness</h2></div><span className="status-pill compliant">82% compliant</span></div><div className="ppe-list"><PPEStatus item="Hard hats" count="154 / 185" /><PPEStatus item="Safety vests" count="169 / 185" /><PPEStatus item="Eye protection" count="143 / 185" status="attention" /><PPEStatus item="Safety boots" count="178 / 185" /></div></section></AppShell>; }
export default PPECompliance;
