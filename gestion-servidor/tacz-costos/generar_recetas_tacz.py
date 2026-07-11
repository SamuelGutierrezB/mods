#!/usr/bin/env python3
"""
Generador de Recetas TaCZ - Actualización Automática de Costos
===============================================================

Script que genera automáticamente todas las recetas de armas y municiones
para el mod TaCZ (Timeless and Classics Zero) basado en un archivo JSON
de costos de entrada.

Uso:
    python generar_recetas_tacz.py <ruta_json_costos>

Ejemplo:
    python generar_recetas_tacz.py "NUEVOS_COSTOS_ARMAS.json"

Requiere:
    - Python 3.7+
    - El archivo JSON de costos debe estar en la misma carpeta que este script
    - MAPEO_MATERIALES_NUEVOS_TACZ.json debe existir en la misma carpeta que este script
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

# Materiales soportados por TaCZ
MATERIALES_SOPORTADOS = {
    'hierro', 'oro', 'cobre', 'netherita',
    'diamante', 'lapislazuli', 'cuarzo', 'amatista',
    'polvo_redstone', 'polvo_glowstone',
    'pólvora', 'pepita_hierro', 'vara_blaze',
    'madera'
}

MATERIALES_NO_SOPORTADOS = {
    'carbon', 'bloque_magma', 'bloque_netherite', 'bloque_oro'
}


class GeneradorRecetasTaCZ:
    """Generador automático de recetas para TaCZ"""

    def __init__(self, ruta_mods: str):
        """
        Inicializar el generador

        Args:
            ruta_mods: Ruta a la carpeta /mods/ de Minecraft
        """
        self.ruta_mods = Path(ruta_mods)
        self.ruta_mapeo = self.ruta_mods / 'MAPEO_MATERIALES_NUEVOS_TACZ.json'
        self.diccionario_forge = {}
        self.errores = []
        self.advertencias = []

    def cargar_mapeo(self) -> bool:
        """Cargar el mapeo de materiales"""
        if not self.ruta_mapeo.exists():
            self.errores.append(f"Mapeo no encontrado: {self.ruta_mapeo}")
            return False

        try:
            with open(self.ruta_mapeo, 'r', encoding='utf-8') as f:
                mapeo = json.load(f)
                self.diccionario_forge = mapeo.get('diccionario_forge', {})

            print(f"[OK] Mapeo cargado: {len(self.diccionario_forge)} materiales")
            return True
        except Exception as e:
            self.errores.append(f"Error cargando mapeo: {e}")
            return False

    def validar_material(self, material: str, arma_nombre: str) -> bool:
        """
        Validar si un material es soportado

        Returns:
            True si es válido, False si no
        """
        if material in MATERIALES_NO_SOPORTADOS:
            self.advertencias.append(
                f"Material no soportado '{material}' removido de {arma_nombre}"
            )
            return False

        if material not in self.diccionario_forge:
            self.errores.append(
                f"Material desconocido '{material}' en {arma_nombre}"
            )
            return False

        return True

    def generar_receta_arma(self, arma: Dict[str, Any]) -> Dict[str, Any]:
        """Generar receta JSON para un arma"""
        nombre = arma.get('nombre', 'Desconocida')
        gun_id = arma.get('id', '')
        materiales = arma.get('materiales', {})

        materials = []
        for material_nombre, cantidad in materiales.items():
            if self.validar_material(material_nombre, nombre):
                tag = self.diccionario_forge[material_nombre]
                materials.append({
                    "item": {"tag": tag},
                    "count": cantidad
                })

        return {
            "materials": materials,
            "result": {
                "type": "gun",
                "id": gun_id
            },
            "type": "tacz:gun_smith_table_crafting"
        }

    def generar_receta_municion(self, municion: Dict[str, Any]) -> Dict[str, Any]:
        """Generar receta JSON para una munición"""
        nombre = municion.get('nombre', 'Desconocida')
        ammo_id = municion.get('id', '')
        grupo = municion.get('grupo', '')
        cantidad = municion.get('cantidad_producida', 1)
        materiales = municion.get('materiales', {})

        materials = []
        for material_nombre, cantidad_mat in materiales.items():
            if self.validar_material(material_nombre, nombre):
                tag = self.diccionario_forge[material_nombre]
                materials.append({
                    "item": {"tag": tag},
                    "count": cantidad_mat
                })

        return {
            "materials": materials,
            "result": {
                "type": "ammo",
                "group": grupo,
                "id": ammo_id,
                "count": cantidad
            },
            "type": "tacz:gun_smith_table_crafting"
        }

    def generar_diccionario_recetas_armas(self, datos: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Generar {nombre_archivo: receta} para todas las armas, sin tocar disco"""
        recetas = {}

        for categoria, armas in datos.get('tabla_costos', {}).items():
            for arma in armas:
                try:
                    receta = self.generar_receta_arma(arma)
                    gun_id = arma.get('id', '')
                    archivo_nombre = gun_id.split(':')[1] + '.json'
                    recetas[archivo_nombre] = receta
                except Exception as e:
                    self.errores.append(
                        f"Error procesando arma {arma.get('nombre')}: {e}"
                    )

        return recetas

    def generar_diccionario_recetas_municiones(self, datos: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Generar {nombre_archivo: receta} para todas las municiones, sin tocar disco"""
        recetas = {}

        for categoria, municiones in datos.get('tabla_costos_municiones', {}).items():
            for municion in municiones:
                try:
                    receta = self.generar_receta_municion(municion)
                    ammo_id = municion.get('id', '')
                    archivo_nombre = ammo_id.split(':')[1] + '.json'
                    recetas[archivo_nombre] = receta
                except Exception as e:
                    self.errores.append(
                        f"Error procesando municion {municion.get('nombre')}: {e}"
                    )

        return recetas

    def procesar_armas(self, datos: Dict[str, Any], ruta_salida: Path) -> int:
        """
        Procesar y guardar todas las armas

        Returns:
            Número de armas procesadas
        """
        recetas = self.generar_diccionario_recetas_armas(datos)
        ruta_salida.mkdir(parents=True, exist_ok=True)

        for archivo_nombre, receta in recetas.items():
            with open(ruta_salida / archivo_nombre, 'w', encoding='utf-8') as f:
                json.dump(receta, f, indent=2, ensure_ascii=False)

        return len(recetas)

    def procesar_municiones(self, datos: Dict[str, Any], ruta_salida: Path) -> int:
        """
        Procesar y guardar todas las municiones

        Returns:
            Número de municiones procesadas
        """
        recetas = self.generar_diccionario_recetas_municiones(datos)
        ruta_salida.mkdir(parents=True, exist_ok=True)

        for archivo_nombre, receta in recetas.items():
            with open(ruta_salida / archivo_nombre, 'w', encoding='utf-8') as f:
                json.dump(receta, f, indent=2, ensure_ascii=False)

        return len(recetas)

    def generar_recetas(self, ruta_json_costos: str) -> bool:
        """
        Proceso principal: generar todas las recetas

        Args:
            ruta_json_costos: Ruta al archivo JSON de costos

        Returns:
            True si fue exitoso, False si hubo errores
        """
        # 1. Cargar mapeo
        if not self.cargar_mapeo():
            return False

        # 2. Cargar costos
        ruta_costos = self.ruta_mods / ruta_json_costos
        if not ruta_costos.exists():
            self.errores.append(f"Archivo de costos no encontrado: {ruta_costos}")
            return False

        print(f"\n[OK] Cargando costos desde: {ruta_costos}")

        try:
            with open(ruta_costos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except Exception as e:
            self.errores.append(f"Error cargando JSON de costos: {e}")
            return False

        # 3. Determinar si es armas o municiones
        es_armas = 'tabla_costos' in datos
        es_municiones = 'tabla_costos_municiones' in datos

        # 4. Determinar rutas de salida
        ruta_tacz = Path(str(self.ruta_mods).replace('/mods', '/tacz/tacz_default_gun'))
        ruta_gun = ruta_tacz / 'data' / 'tacz' / 'recipes' / 'gun'
        ruta_ammo = ruta_tacz / 'data' / 'tacz' / 'recipes' / 'ammo'

        # 5. Procesar armas
        armas_procesadas = 0
        if es_armas:
            armas_procesadas = self.procesar_armas(datos, ruta_gun)
            print(f"[OK] {armas_procesadas} armas generadas")

        # 6. Procesar municiones
        municiones_procesadas = 0
        if es_municiones:
            municiones_procesadas = self.procesar_municiones(datos, ruta_ammo)
            print(f"[OK] {municiones_procesadas} municiones generadas")

        # 7. Mostrar resultados
        print(f"\n[RESULTADO]")
        print(f"  Armas: {armas_procesadas}")
        print(f"  Municiones: {municiones_procesadas}")
        print(f"  Total: {armas_procesadas + municiones_procesadas}")

        if self.advertencias:
            print(f"\n[ADVERTENCIAS] ({len(self.advertencias)})")
            for adv in self.advertencias[:10]:  # Mostrar primeras 10
                print(f"  - {adv}")
            if len(self.advertencias) > 10:
                print(f"  ... y {len(self.advertencias) - 10} más")

        if self.errores:
            print(f"\n[ERRORES] ({len(self.errores)})")
            for err in self.errores[:10]:
                print(f"  - {err}")
            if len(self.errores) > 10:
                print(f"  ... y {len(self.errores) - 10} más")
            return False

        print(f"\n[EXITO] Todas las recetas generadas correctamente")
        return True


def main():
    """Función principal"""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUso: python script.py <archivo_json>")
        print("  Ejemplo: python script.py NUEVOS_COSTOS_ARMAS.json")
        sys.exit(1)

    archivo_json = sys.argv[1]

    # Detectar carpeta del script (debe contener el mapeo)
    ruta_script = Path(__file__).parent

    if (ruta_script / 'MAPEO_MATERIALES_NUEVOS_TACZ.json').exists():
        ruta_mods = ruta_script
    else:
        print("[ERROR] No se encontró MAPEO_MATERIALES_NUEVOS_TACZ.json")
        print("Coloca el script en la misma carpeta que MAPEO_MATERIALES_NUEVOS_TACZ.json")
        sys.exit(1)

    generador = GeneradorRecetasTaCZ(str(ruta_mods))
    exito = generador.generar_recetas(archivo_json)

    sys.exit(0 if exito else 1)


if __name__ == '__main__':
    main()
