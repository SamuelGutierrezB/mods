# Contexto del proyecto

Repo de mods de Minecraft 1.20.1 Forge (temática medieval + magia + dimensiones) que también gestiona un servidor dedicado en la nube. Ver [gestion-servidor/documentacion/README.md](gestion-servidor/documentacion/README.md) para el catálogo de mods y [gestion-servidor/documentacion/CONTEXTO_SERVIDOR.md](gestion-servidor/documentacion/CONTEXTO_SERVIDOR.md) para el estado del servidor (IP, infra, pendientes).

## ⚠️ Esta carpeta es a la vez el repo git Y la carpeta viva de mods del cliente local

`C:\Users\samue\AppData\Roaming\.minecraft\mods\` es simultáneamente:
1. El working directory del repo git
2. La carpeta real que usa el launcher de Minecraft del usuario para cargar mods

**Nunca uses `git rm` a secas sobre un `.jar`** — borra el archivo físico y rompe la instalación local del usuario. Usa `git rm --cached` si solo quieres sacarlo del tracking de una rama mientras conservas el archivo en disco.

## Ramas

- **`main`**: base del proyecto.
- **`server`**: la que se hace `pull` en la VM del servidor, nada más. Solo tiene los mods necesarios server-side (no HUD/render/minimapa/audio/recetas-cliente) — **sin** herramientas de gestión ni docs, no las necesita.
- **`client-modpack`**: copia completa (67 mods) que jalan los jugadores para conectarse. Sin herramientas de gestión.
- **`admin`**: para quien administra el servidor. Tiene el modpack completo (67 mods, igual que `client-modpack`) **más** las herramientas de `gestion-servidor/` (scripts de conexión, docs, este mismo `CLAUDE.md`). Es la rama de referencia para trabajar en la gestión del servidor.
- **`feature/guns-coast`**, **`optimized-jet`**: en desarrollo, no relacionadas con la gestión del servidor.

Al agregar o quitar mods de `server`, replicá el cambio también en `client-modpack` y `admin` para que las tres listas de mods no diverjan sin querer. Las claves SSH (`*.key`, `*.key.pub`) NUNCA se suben a ninguna rama — están en `.gitignore`.

## Servidor dedicado

Detalles completos en [CONTEXTO_SERVIDOR.md](gestion-servidor/documentacion/CONTEXTO_SERVIDOR.md). Resumen rápido:

- OCI, Ubuntu 24.04 ARM64 (Ampere/Neoverse-N1), IP `163.192.149.131`, usuario `ubuntu`.
- Java **17** obligatorio (no 21) para Forge 1.20.1.
- Firewall del SO es `iptables` (no `ufw`), persistido con `netfilter-persistent`. OCI también tiene firewall a nivel de VCN (Security List/NSG) — si algo no conecta desde fuera, revisar ahí también, no solo iptables.
- Servidor Forge instalado en `~/minecraft/`, corre con `run.sh nogui`, 8 GB de RAM asignados.
- Conexión SSH: alias `ssh mc-server` (config en `~/.ssh/config` local, fuera del repo) o script en `gestion-servidor/acceso/conectar.ps1`.
- ⚠️ **La clave privada no está en el repo.** Para que `conectar.ps1` (o el alias SSH) funcione, hay que colocar manualmente la clave en `gestion-servidor/ssh-key-2026-07-17.key` — ver [gestion-servidor/acceso/README.md](gestion-servidor/acceso/README.md).
- Pendiente: `systemd`/`screen` para consola persistente y arranque automático; sincronizar mods de la rama `server` al servidor; subir `view-distance`/`simulation-distance` en `server.properties` (están en default, muy cortos para este modpack).

## Convenciones

- Mensajes de commit en inglés (regla global del usuario), aunque la conversación sea en español.
- Documentación del catálogo de mods sigue el formato de [MODS_JAVA_PROPUESTOS.md](gestion-servidor/documentacion/MODS_JAVA_PROPUESTOS.md).
