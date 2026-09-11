import React, { useState } from "react";
import { Link } from "react-router-dom";
import { requestPasswordReset } from "../services/authService.js";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const submit = async (event) => { event.preventDefault(); const result = await requestPasswordReset(email); setMessage(result.message); };
  return <main className="auth-page"><form className="auth-card" onSubmit={submit}><span className="brand-mark large">B</span><h1>Reset your password</h1><p>Enter your work email to request reset instructions.</p><label>Email<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required /></label><button className="primary-button" type="submit">Send instructions</button>{message && <div className="form-success">{message}</div>}<Link className="form-link" to="/login">Back to sign in</Link></form></main>;
}

export default ForgotPassword;
