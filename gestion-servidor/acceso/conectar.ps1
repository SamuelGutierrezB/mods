$keyPath = Join-Path $PSScriptRoot "..\ssh-key-2026-07-17.key"
$ip = "163.192.149.131"
$usuario = "ubuntu"

if (-not (Test-Path $keyPath)) {
    Write-Error "No se encontro la clave privada en $keyPath. Copia ahi tu clave SSH (ver README.md de esta carpeta) antes de conectar."
    exit 1
}

ssh -i $keyPath "$usuario@$ip"
