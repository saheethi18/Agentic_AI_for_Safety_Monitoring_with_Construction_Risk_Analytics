import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { signup } from "../services/authService.js";

function Signup() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [error, setError] = useState("");
  const submit = async (event) => { event.preventDefault(); try { await signup(form.name, form.email, form.password); navigate("/dashboard", { replace: true }); } catch (submissionError) { setError(submissionError.message); } };
  return <main className="auth-page"><form className="auth-card" onSubmit={submit}><span className="brand-mark large">B</span><h1>Create your account</h1><p>Set up your BuildSure safety workspace</p>{error && <div className="form-error">{error}</div>}<label>Name<input value={form.name} onChange={(event) => setForm({ ...form, name: event.target.value })} required /></label><label>Email<input type="email" value={form.email} onChange={(event) => setForm({ ...form, email: event.target.value })} required /></label><label>Password<input type="password" value={form.password} onChange={(event) => setForm({ ...form, password: event.target.value })} required /></label><button className="primary-button" type="submit">Create account</button><div className="auth-footer">Already registered? <Link to="/login">Sign in</Link></div></form></main>;
}

export default Signup;
