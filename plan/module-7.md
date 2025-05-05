# 📘 Module 7: Secrets & Secure Auth

| Submodule                 | Study | Project | Difficulty |
| ------------------------- | ----- | ------- | ---------- |
| 7.1 OAuth2 & JWT          | 6h    | 3h      | I–A        |
| 7.2 Secure Secrets Access | 5h    | 3h      | I–A        |
| 7.3 HTTPS & TLS Config    | 4h    | 2h      | I          |

### 7.1 OAuth2 & JWT

| Item                   | Description               | Learning Objectives                       | Micro-Project                             | Study | Build | Level |
| ---------------------- | ------------------------- | ----------------------------------------- | ----------------------------------------- | ----- | ----- | ----- |
| 7.1.1 OAuth2 Flow      | Authorization code + PKCE | - Secure login with public clients        | OAuth2 login with GitHub                  | 2h    | 1.5h  | I     |
| 7.1.2 JWT Structure    | Encoded identity + claims | - Understand tokens, verify signatures    | Token inspector CLI                       | 2h    | 1h    | I     |
| 7.1.3 Refresh & Revoke | Long-lived sessions       | - Manage refresh tokens + revocation list | Auth API with access + refresh token flow | 2h    | 0.5h  | A     |

**Branch Project 7.1:** Auth & Claims API – Login API using OAuth2, JWT access tokens, and scope-based authorization.

### 7.2 Secure Secrets Access

| Item                  | Description                  | Learning Objectives                        | Micro-Project                            | Study | Build | Level |
| --------------------- | ---------------------------- | ------------------------------------------ | ---------------------------------------- | ----- | ----- | ----- |
| 7.2.1 Vault Basics    | Secure KV store              | - Store/retrieve application credentials   | Secure FastAPI secrets loader            | 2h    | 1.5h  | I     |
| 7.2.2 Dynamic Secrets | Ephemeral DB/API keys        | - Generate, expire, and rotate credentials | Vault role-based DB credential issuer    | 2h    | 1h    | A     |
| 7.2.3 AppRole Auth    | Identity-based secret access | - Grant scoped access via AppRoles         | CLI tool to authenticate and pull tokens | 1h    | 0.5h  | A     |

**Branch Project 7.2:** Secrets-Aware Service – Service pulling DB credentials and API keys securely via Vault.

### 7.3 HTTPS & TLS Config

| Item                  | Description                      | Learning Objectives                      | Micro-Project                              | Study | Build | Level |
| --------------------- | -------------------------------- | ---------------------------------------- | ------------------------------------------ | ----- | ----- | ----- |
| 7.3.1 Self-Signed TLS | Local HTTPS for dev              | - Create TLS certs, trust locally        | HTTPS FastAPI app with self-signed certs   | 2h    | 1h    | I     |
| 7.3.2 Certbot + NGINX | Auto-renewing TLS for production | - Use Certbot with webserver integration | TLS-secured static site with Let's Encrypt | 2h    | 1h    | I     |

**Branch Project 7.3:** Secure Gateway Proxy – HTTPS-secured reverse proxy using NGINX and Certbot.

**Capstone 7:** Auth Gateway Stack – OAuth2 secured service using JWT, secrets pulled from Vault, running behind HTTPS with TLS certs and secure headers.
