# 🌐 Official Custom Domain Setup Guide: TKRCET Campus Recovery Portal

This guide explains how to map a permanent, branded custom domain (e.g. **`recovery.tkrcet.ac.in`** or your own custom domain) to this portal using **Cloudflare Named Tunnels (Zero Trust)**.

---

## 🚀 Why Use a Named Tunnel Instead of `trycloudflare.com`?

| Feature | Quick Tunnel (`trycloudflare.com`) | Named Tunnel (`recovery.tkrcet.ac.in`) |
| :--- | :--- | :--- |
| **Domain** | Random temporary hash (e.g. `guidance-firewall...`) | Clean, official institutional branded domain |
| **Persistence** | Resets on restart / disconnect | Permanent, 99.99% uptime |
| **SSL / TLS** | Standard Cloudflare cert | Institutional certificate + HSTS preload |
| **Security** | Public edge | Zero-Trust firewall, IP filtering, DDoS shield |

---

## 🛠️ Step-by-Step Production Setup (Takes 3 Minutes)

### 1. Authenticate Cloudflared with Your College Domain
Run this command in PowerShell:
```powershell
.\cloudflared.exe tunnel login
```
*A browser window will open asking you to select your domain (e.g. `tkrcet.ac.in` or any domain registered on Cloudflare).*

### 2. Create the Permanent Named Tunnel
```powershell
.\cloudflared.exe tunnel create tkrcet-campus-recovery
```
*This generates a permanent Tunnel ID (UUID) and creates an encrypted credentials file in `~/.cloudflared/`.*

### 3. Route Your Custom Subdomain (DNS CNAME)
```powershell
.\cloudflared.exe tunnel route dns tkrcet-campus-recovery recovery.tkrcet.ac.in
```
*Cloudflare automatically creates a CNAME DNS record pointing `recovery.tkrcet.ac.in` to your encrypted tunnel.*

### 4. Run the Permanent Tunnel Service
```powershell
.\cloudflared.exe tunnel run --url http://localhost:8501 tkrcet-campus-recovery
```

To run it as an automatic Windows Background Service that restarts on reboot:
```powershell
.\cloudflared.exe service install
Start-Service cloudflared
```
