export function login(request, response) { const { email } = request.body; response.json({ user: { id: "local-user", name: email?.split("@")[0] || "Safety Officer", email } }); }
export function signup(request, response) { const { name, email } = request.body; response.status(201).json({ user: { id: "local-user", name, email } }); }
export function forgotPassword(_request, response) { response.json({ message: "If an account exists, reset instructions will be sent." }); }
