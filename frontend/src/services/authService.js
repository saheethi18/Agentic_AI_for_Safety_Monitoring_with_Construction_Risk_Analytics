const SESSION_KEY = "buildsure.session";

export function getCurrentUser() {
  try {
    return JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
  } catch {
    return null;
  }
}

export function isAuthenticated() {
  return Boolean(getCurrentUser());
}

export function createSession(user) {
  const session = { id: user.id || "local-user", name: user.name, email: user.email };
  localStorage.setItem(SESSION_KEY, JSON.stringify(session));
  return session;
}

export function clearSession() {
  localStorage.removeItem(SESSION_KEY);
}

export async function login(email, password) {
  if (!email || !password) throw new Error("Email and password are required.");
  return createSession({ name: email.split("@")[0], email });
}

export async function signup(name, email, password) {
  if (!name || !email || !password) throw new Error("All fields are required.");
  return createSession({ name, email });
}

export async function requestPasswordReset(email) {
  if (!email) throw new Error("Email is required.");
  return { message: "If an account exists, reset instructions will be sent." };
}
