#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para actualizar automáticamente las recetas de TaCZ con nuevos costos y Forge tags
"""

import json
import os
from pathlib import Path

# Configuración
MODS_DIR = Path(__file__).parent
NUEVOS_COSTOS = MODS_DIR / "NUEVOS_COSTOS_ARMAS.json"
NUEVOS_COSTOS_BALAS = MODS_DIR / "NUEVOS_COSTOS_BALAS.json"
MAPEO_MATERIALES = MODS_DIR / "MAPEO_MATERIALES_NUEVOS_TACZ.json"
TACZ_DIR = Path.home() / "AppData" / "Roaming" / ".minecraft" / "tacz" / "tacz_default_gun" / "data" / "tacz" / "recipes"
GUN_DIR = TACZ_DIR / "gun"
AMMO_DIR = TACZ_DIR / "ammo"

# Mapeo corregido: Estructura correcta con "item" envuelto
MATERIALES_DEF = {
    "hierro": {"item": {"tag": "forge:ingots/iron"}},
    "oro": {"item": {"tag": "forge:ingots/gold"}},
    "cobre": {"item": {"tag": "forge:ingots/copper"}},
    "netherita": {"item": {"tag": "forge:ingots/netherite"}},
    "diamante": {"item": {"tag": "forge:gems/diamond"}},
    "lapislazuli": {"item": {"tag": "forge:gems/lapis"}},
    "cuarzo": {"item": {"tag": "forge:gems/quartz"}},
    "amatista": {"item": {"tag": "forge:gems/amethyst"}},
    "carbon": {"item": "minecraft:coal"},
    "polvo_redstone": {"item": {"tag": "forge:dusts/redstone"}},
    "polvo_glowstone": {"item": {"tag": "forge:dusts/glowstone"}},
    "madera": {"item": {"tag": "minecraft:logs"}},
    "pólvora": {"item": {"tag": "forge:gunpowder"}},
    "pepita_hierro": {"item": {"tag": "forge:nuggets/iron"}},
    "vara_blaze": {"item": {"tag": "forge:rods/blaze"}},
    "bloque_magma": {"item": "minecraft:magma_block"},
    "bloque_netherite": {"item": {"tag": "forge:storage_blocks/netherite"}},
    "bloque_oro": {"item": {"tag": "forge:storage_blocks/gold"}}
}

def load_json(filepath):
    """Carga un archivo JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_recipe_json(gun_id, materials):
    """Crea el JSON de receta con estructura correcta para ítems o tags"""
    recipe = {
        "materials": [],
        "result": {
            "type": "gun",
            "id": gun_id
        },
        "type": "tacz:gun_smith_table_crafting"
    }
    
    for mat_name, count in materials.items():
        if count > 0 and mat_name in MATERIALES_DEF:
            # Copiamos la definición (sea "tag" o "item") y le agregamos la cantidad
            material_entry = MATERIALES_DEF[mat_name].copy()
            material_entry["count"] = count
            recipe["materials"].append(material_entry)
    
    return recipe

def create_ammo_recipe_json(ammo_id, materials):
    """Crea el JSON de receta para munición con estructura correcta"""
    recipe = {
        "materials": [],
        "result": {
            "type": "ammo",
            "id": ammo_id
        },
        "type": "tacz:gun_smith_table_crafting"
    }
    
    for mat_name, count in materials.items():
        if count > 0 and mat_name in MATERIALES_DEF:
            material_entry = MATERIALES_DEF[mat_name].copy()
            material_entry["count"] = count
            recipe["materials"].append(material_entry)
    
    return recipe

def update_weapon_recipes():
    """Actualiza todas las recetas de armas"""
    costos = load_json(NUEVOS_COSTOS)
    tabla_costos = costos["tabla_costos"]
    
    contador = 0
    
    # Procesar pistolas
    for weapon in tabla_costos["pistolas"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar rifles de asalto
    for weapon in tabla_costos["rifles_asalto"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar rifles de francotirador
    for weapon in tabla_costos["rifles_francotirador"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar escopetas
    for weapon in tabla_costos["escopetas"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar subfusiles
    for weapon in tabla_costos["subfusiles"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar rifles ametralladora
    for weapon in tabla_costos["rifles_metralleta"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar especiales
    for weapon in tabla_costos["especiales"]:
        filename = weapon["id"].split(":")[-1] + ".json"
        filepath = GUN_DIR / filename
        recipe = create_recipe_json(weapon["id"], weapon["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    return contador

def update_ammo_recipes():
    """Actualiza todas las recetas de munición"""
    costos = load_json(NUEVOS_COSTOS_BALAS)
    tabla_costos = costos["tabla_costos_municiones"]
    
    contador = 0
    
    # Procesar pistola cartuchos
    for ammo in tabla_costos["pistola_cartuchos"]:
        filename = ammo["id"].split(":")[-1] + ".json"
        filepath = AMMO_DIR / filename
        recipe = create_ammo_recipe_json(ammo["id"], ammo["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar rifle cartuchos
    for ammo in tabla_costos["rifle_cartuchos"]:
        filename = ammo["id"].split(":")[-1] + ".json"
        filepath = AMMO_DIR / filename
        recipe = create_ammo_recipe_json(ammo["id"], ammo["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar escopeta cartuchos
    for ammo in tabla_costos["escopeta_cartuchos"]:
        filename = ammo["id"].split(":")[-1] + ".json"
        filepath = AMMO_DIR / filename
        recipe = create_ammo_recipe_json(ammo["id"], ammo["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    # Procesar explosivos
    for ammo in tabla_costos["explosivos"]:
        filename = ammo["id"].split(":")[-1] + ".json"
        filepath = AMMO_DIR / filename
        recipe = create_ammo_recipe_json(ammo["id"], ammo["materiales"])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
        print(f"✓ Actualizado: {filename}")
        contador += 1
    
    return contador

def main():
    print("=" * 60)
    print("Script de Actualización de Recetas TaCZ")
    print("=" * 60)
    print()
    
    # Verificar archivos necesarios
    if not NUEVOS_COSTOS.exists():
        print(f"ERROR: No existe {NUEVOS_COSTOS}")
        return
    
    if not NUEVOS_COSTOS_BALAS.exists():
        print(f"ERROR: No existe {NUEVOS_COSTOS_BALAS}")
        return
    
    if not GUN_DIR.exists():
        print(f"ERROR: Directorio de armas no existe: {GUN_DIR}")
        return
    
    if not AMMO_DIR.exists():
        print(f"ERROR: Directorio de munición no existe: {AMMO_DIR}")
        return
    
    print(f"📁 Directorio de armas: {GUN_DIR}")
    print(f"📁 Directorio de munición: {AMMO_DIR}")
    print()
    
    # Actualizar armas
    print("🔧 Actualizando armas...")
    contador_armas = update_weapon_recipes()
    
    print()
    print("🔧 Actualizando municiones...")
    contador_ammo = update_ammo_recipes()
    
    print()
    print("=" * 60)
    print(f"✅ Completado: {contador_armas} armas + {contador_ammo} municiones")
    print("=" * 60)
    print()
    print("Cambios aplicados:")
    print("  • Nuevos costos de materiales")
    print("  • Todos los materiales usando Forge tags")
    print("  • minecraft:logs → forge:logs")
    print("  • Nuevos materiales: carbón, polvo_redstone, polvo_glowstone, etc.")

if __name__ == "__main__":
    main()

