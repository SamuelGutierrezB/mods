# Contexto del servidor - Minecraft 1.20.1 Forge

Notas operativas del servidor para retomar trabajo sin tener que re-descubrir todo desde cero.

## Infraestructura

- **Proveedor:** Oracle Cloud Infrastructure (OCI)
- **IP pública:** `163.192.149.131`
- **Usuario SSH:** `ubuntu`
- **Acceso:** clave privada en `gestion-servidor/ssh-key-2026-07-17.key` (no está en el repo, ver `acceso/`)
- **CPU:** 4 vCPU Ampere Neoverse-N1 (**ARM64/aarch64**, no x86)
- **RAM:** 23 GB total
- **Disco:** 96 GB (`/dev/sda1` en `/`)
- **OS:** Ubuntu 24.04.4 LTS, kernel `6.17.0-1011-oracle`
- **Región:** mx-queretaro (mirrors `ports.ubuntu.com` por ser ARM)

## Red / Firewall

- Firewall del SO: `iptables` (no `ufw`, no está instalado). Persistencia con `iptables-persistent` / `netfilter-persistent save`.
- Puertos abiertos: `22/tcp` (SSH, ya venía abierto), `25565/tcp` (Minecraft, agregado).
- **Importante:** además del iptables local, OCI tiene su propio firewall a nivel de nube (Security List / NSG de la VCN). Si algo deja de responder desde fuera, revisar también ahí, no solo iptables.
- La salida a internet (egress) tuvo un corte temporal por configuración de VCN (Internet Gateway / Route Table); si vuelve a fallar `apt`/`wget`, revisar eso primero con `ping 8.8.8.8` y `curl -4 -m 5 -sI http://algo`.

## Servidor de Minecraft

- **Modloader:** Forge **1.20.1-47.4.20** (misma build que el cliente local en `launcher_profiles.json`)
- **Java:** OpenJDK **17** (ARM64) — NO usar Java 21, Forge 1.20.1 requiere 17
- **Ruta:** `~/minecraft/` en el servidor
- **RAM asignada:** 8 GB (`-Xmx8G -Xms8G` en `user_jvm_args.txt`)
- **Arranque:** `~/minecraft/run.sh nogui`
- **Mundo:** `~/minecraft/world/`, `level-name=world`, semilla aleatoria, `level-type=normal`, `difficulty=easy`, `gamemode=survival`, `online-mode=true`, `max-players=20`
- **EULA:** aceptado (`eula.txt`)

### Pendiente / siguiente paso

- El servidor se arrancó con `nohup ... & disown` — **no hay consola interactiva** para dar comandos (`/op`, `/stop`, etc.) ni arranque automático si el proceso muere o la VM reinicia.
- Falta configurar `systemd` (o `screen`/`tmux`) para administración persistente.
- Falta sincronizar los mods: rama git `server` (solo mods server-side) debe hacerse `pull`/copiar a `~/minecraft/mods/` en la VM.

## Ramas de git relevantes

- **`server`**: rama que se jala en la VM. Contiene solo mods necesarios server-side (se excluyeron 9 mods cliente-only: BetterF3, MouseTweaks, Embeddium, Oculus, Xaero's Minimap, Sound Physics Remastered, JEI, AcceleratedRendering, Highlighter — ver `.gitignore`). También contiene las herramientas de gestión (`gestion-servidor/`), salvo las claves SSH.
- **`client-modpack`**: rama que jalan los jugadores, con el modpack completo (67 mods).
- Las claves SSH (`.key`, `.key.pub`) nunca se suben a ningún branch — están en `.gitignore`.

## Herramientas de acceso

Ver [`acceso/`](../acceso/) para el script de conexión rápida.
