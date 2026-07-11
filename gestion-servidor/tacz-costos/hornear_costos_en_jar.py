#!/usr/bin/env python3
"""
Hornear Costos en el JAR de TaCZ
=================================

Reemplaza las recetas por defecto embebidas dentro del .jar de TaCZ
(assets/tacz/custom/tacz_default_gun/data/tacz/recipes/...) por las
generadas a partir de NUEVOS_COSTOS_ARMAS.json y NUEVOS_COSTOS_BALAS.json.

Con esto, cada vez que Minecraft extraiga el gunpack por defecto (carpeta
.minecraft/tacz/ borrada o instalación nueva), ya vendrá con los costos
configurados aquí, sin necesidad de correr generar_recetas_tacz.py después.

Uso:
    python hornear_costos_en_jar.py

Requiere:
    - generar_recetas_tacz.py en la misma carpeta
    - NUEVOS_COSTOS_ARMAS.json, NUEVOS_COSTOS_BALAS.json,
      MAPEO_MATERIALES_NUEVOS_TACZ.json en la misma carpeta
    - El .jar de TaCZ en .minecraft/mods/ (dos niveles arriba de este script)
"""

import json
import shutil
import sys
import zipfile
from pathlib import Path

from generar_recetas_tacz import GeneradorRecetasTaCZ

RUTA_INTERNA_GUN = "assets/tacz/custom/tacz_default_gun/data/tacz/recipes/gun/"
RUTA_INTERNA_AMMO = "assets/tacz/custom/tacz_default_gun/data/tacz/recipes/ammo/"


def encontrar_jar(ruta_mods: Path) -> Path:
    candidatos = list(ruta_mods.glob("tacz-*.jar"))
    if not candidatos:
        print("[ERROR] No se encontró ningún .jar de TaCZ (tacz-*.jar) en la carpeta mods/")
        sys.exit(1)
    if len(candidatos) > 1:
        print(f"[ERROR] Hay más de un .jar de TaCZ, deja solo uno: {candidatos}")
        sys.exit(1)
    return candidatos[0]


def cargar_json(ruta: Path) -> dict:
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    ruta_script = Path(__file__).parent
    ruta_mods = ruta_script.parent.parent  # .minecraft/mods (ahí vive el .jar, ya no junto al script)
    ruta_jar = encontrar_jar(ruta_mods)

    print(f"[OK] JAR detectado: {ruta_jar.name}")

    generador = GeneradorRecetasTaCZ(str(ruta_script))
    if not generador.cargar_mapeo():
        for err in generador.errores:
            print(f"[ERROR] {err}")
        sys.exit(1)

    datos_armas = cargar_json(ruta_script / "NUEVOS_COSTOS_ARMAS.json")
    datos_balas = cargar_json(ruta_script / "NUEVOS_COSTOS_BALAS.json")

    recetas_gun = generador.generar_diccionario_recetas_armas(datos_armas)
    recetas_ammo = generador.generar_diccionario_recetas_municiones(datos_balas)

    if generador.errores:
        print(f"\n[ERRORES] ({len(generador.errores)}) - se detiene sin tocar el jar")
        for err in generador.errores[:10]:
            print(f"  - {err}")
        sys.exit(1)

    print(f"[OK] {len(recetas_gun)} recetas de armas generadas en memoria")
    print(f"[OK] {len(recetas_ammo)} recetas de municiones generadas en memoria")

    # Verificar que todos los archivos objetivo existan ya dentro del jar
    with zipfile.ZipFile(ruta_jar, 'r') as zf:
        nombres_jar = set(zf.namelist())

    reemplazos = {}
    for nombre, receta in recetas_gun.items():
        ruta_interna = RUTA_INTERNA_GUN + nombre
        if ruta_interna not in nombres_jar:
            print(f"[ADVERTENCIA] {ruta_interna} no existe en el jar, se omite")
            continue
        reemplazos[ruta_interna] = json.dumps(receta, indent=2, ensure_ascii=False).encode('utf-8')

    for nombre, receta in recetas_ammo.items():
        ruta_interna = RUTA_INTERNA_AMMO + nombre
        if ruta_interna not in nombres_jar:
            print(f"[ADVERTENCIA] {ruta_interna} no existe en el jar, se omite")
            continue
        reemplazos[ruta_interna] = json.dumps(receta, indent=2, ensure_ascii=False).encode('utf-8')

    print(f"[OK] {len(reemplazos)} archivos serán reemplazados dentro del jar")

    # Backup del jar original (solo si no existe ya uno)
    ruta_backup = ruta_jar.with_suffix(ruta_jar.suffix + ".backup")
    if not ruta_backup.exists():
        shutil.copy2(ruta_jar, ruta_backup)
        print(f"[OK] Backup creado: {ruta_backup.name}")
    else:
        print(f"[OK] Backup ya existía: {ruta_backup.name} (no se sobreescribe)")

    ruta_temporal = ruta_jar.with_suffix(ruta_jar.suffix + ".tmp")

    with zipfile.ZipFile(ruta_jar, 'r') as zf_in:
        with zipfile.ZipFile(ruta_temporal, 'w', zipfile.ZIP_DEFLATED) as zf_out:
            for item in zf_in.infolist():
                if item.filename in reemplazos:
                    zf_out.writestr(item, reemplazos[item.filename])
                else:
                    zf_out.writestr(item, zf_in.read(item.filename))

    ruta_temporal.replace(ruta_jar)

    print(f"\n[EXITO] JAR actualizado: {ruta_jar.name}")
    print(f"  Armas horneadas: {len(recetas_gun)}")
    print(f"  Municiones horneadas: {len(recetas_ammo)}")
    print(f"\nSi algo sale mal, restaura el backup:")
    print(f"  copy \"{ruta_backup.name}\" \"{ruta_jar.name}\"")


if __name__ == '__main__':
    main()
