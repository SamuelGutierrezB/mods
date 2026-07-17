# Acceso al servidor

## ⚠️ Antes de usar estas herramientas

Las claves SSH **no están en el repo** (están en `.gitignore` a propósito, nunca se suben). Para que `conectar.ps1` funcione, tenés que copiar manualmente la clave privada a:

```
gestion-servidor/ssh-key-2026-07-17.key
```

(y opcionalmente la pública, `ssh-key-2026-07-17.key.pub`, aunque no es necesaria para conectar).

Sin ese archivo ahi, el script falla porque no tiene con qué autenticarse contra el servidor.

## Uso

Desde PowerShell, en la raíz del repo:

```powershell
.\gestion-servidor\acceso\conectar.ps1
```

O directamente con el alias SSH si ya configuraste `~/.ssh/config` (ver [CONTEXTO_SERVIDOR.md](../documentacion/CONTEXTO_SERVIDOR.md)):

```powershell
ssh mc-server
```

Datos de conexión: usuario `ubuntu`, IP `163.192.149.131`. Más contexto del servidor en [CONTEXTO_SERVIDOR.md](../documentacion/CONTEXTO_SERVIDOR.md).
