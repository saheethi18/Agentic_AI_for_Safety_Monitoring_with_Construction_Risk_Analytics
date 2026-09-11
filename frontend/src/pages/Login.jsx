import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { login } from "../services/authService.js";

function Login() {
  const navigate = useNavigate();
  const location = useLocation();
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");

  const submit = async (event) => {
    event.preventDefault();
    try {
      await login(form.email, form.password);
      navigate(location.state?.from || "/dashboard", { replace: true });
    } catch (submissionError) {
      setError(submissionError.message);
    }
  };

  return <AuthPage title="Welcome back" subtitle="Sign in to your safety workspace" onSubmit={submit} fields={form} setFields={setForm} error={error} submitLabel="Sign in" footer={<span>New here? <Link to="/signup">Create an account</Link></span>} />;
}

function AuthPage({ title, subtitle, onSubmit, fields, setFields, error, submitLabel, footer }) {
  return <main className="auth-page"><form className="auth-card" onSubmit={onSubmit}><span className="brand-mark large">B</span><h1>{title}</h1><p>{subtitle}</p>{error && <div className="form-error">{error}</div>}<label>Email<input type="email" value={fields.email} onChange={(event) => setFields({ ...fields, email: event.target.value })} required /></label><label>Password<input type="password" value={fields.password} onChange={(event) => setFields({ ...fields, password: event.target.value })} required /></label><button className="primary-button" type="submit">{submitLabel}</button><Link className="form-link" to="/forgot-password">Forgot password?</Link><div className="auth-footer">{footer}</div></form></main>;
}

export default Login;
