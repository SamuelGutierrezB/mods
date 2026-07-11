# Guía: Actualización de Costos de Armas y Municiones TaCZ

## Problema Original

El mod TaCZ (Timeless and Classics Zero) en Minecraft 1.20.1 tenía costos de crafting simplificados (solo hierro principalmente). Se necesitaba actualizar a costos más complejos con múltiples materiales.

## Solución Implementada

Script automático que genera recetas JSON basadas en un archivo de costos de entrada.

---

## 1. Materiales Soportados por TaCZ

Solo estos materiales pueden usarse como ingredientes de crafting en TaCZ:

### Metales (Forge Tags)

- `forge:ingots/iron` - Hierro
- `forge:ingots/gold` - Oro
- `forge:ingots/copper` - Cobre
- `forge:ingots/netherite` - Netherita

### Gemas (Forge Tags)

- `forge:gems/diamond` - Diamante
- `forge:gems/lapis` - Lapislazuli
- `forge:gems/quartz` - Cuarzo
- `forge:gems/amethyst` - Amatista

### Polvos (Forge Tags - NOTA: plural "dusts")

- `forge:dusts/redstone` - Polvo de Redstone
- `forge:dusts/glowstone` - Polvo de Glowstone

### Otros (Forge Tags)

- `forge:gunpowder` - Pólvora
- `forge:nuggets/iron` - Pepita de Hierro
- `forge:rods/blaze` - Vara de Blaze

### Items Vanilla (Minecraft Tags)

- `minecraft:logs` - Madera/Troncos
- `minecraft:coal` - Carbón

### ⛔ NO SOPORTADOS (Eliminados)

- ~~`carbon`~~ → Mod no lo soporta aunque existe en Minecraft
- ~~`bloque_magma`~~ → No se puede usar como ingrediente
- ~~`bloque_netherite`~~ → No se puede usar como ingrediente
- ~~`bloque_oro`~~ → No se puede usar como ingrediente

---

## 2. Estructura del Proceso

### Paso 1: Entrada JSON de Costos

Archivo: `NUEVOS_COSTOS_ARMAS.json`

```json
{
  "tabla_costos": {
    "pistolas": [
      {
        "nombre": "CZ75",
        "id": "tacz:cz75",
        "materiales": {
          "hierro": 16,
          "madera": 6
        }
      }
    ]
  }
}
```

### Paso 2: Mapeo de Materiales

Archivo: `MAPEO_MATERIALES_NUEVOS_TACZ.json`

Mapea nombres simplificados a etiquetas Forge:

```json
{
  "diccionario_forge": {
    "hierro": "forge:ingots/iron",
    "oro": "forge:ingots/gold",
    "madera": "minecraft:logs",
    ...
  }
}
```

### Paso 3: Generación de Recetas

El script convierte:

```json
// ENTRADA
{
  "nombre": "CZ75",
  "id": "tacz:cz75",
  "materiales": {
    "hierro": 16,
    "madera": 6
  }
}
```

A:

```json
// SALIDA (.json en /recipes/gun/)
{
  "materials": [
    {
      "item": { "tag": "forge:ingots/iron" },
      "count": 16
    },
    {
      "item": { "tag": "minecraft:logs" },
      "count": 6
    }
  ],
  "result": {
    "type": "gun",
    "id": "tacz:cz75"
  },
  "type": "tacz:gun_smith_table_crafting"
}
```

---

## 3. Validaciones Aplicadas

✓ **Verificación de etiquetas Forge correctas**

- Confirmadas contra recetas existentes en TaCZ
- Corregidos: `forge:dust/` → `forge:dusts/` (plural)
- Corregidos: `forge:logs` → `minecraft:logs` (vanilla tag)

✓ **Eliminación de materiales no soportados**

- Verificado contra recetas originales (COSTOS_ARMAS_TACZ.json)
- Removido: carbon (54 referencias)
- Removido: bloque_magma (46 referencias)
- Removido: bloque_netherite (12 referencias)
- Removido: bloque_oro (1 referencia)

✓ **Generación automática**

- 53 armas procesadas
- 24 municiones procesadas
- 100% de recetas regeneradas

---

## 4. Directorios Afectados

**Entrada:**

```
.minecraft/mods/
├── NUEVOS_COSTOS_ARMAS.json
├── NUEVOS_COSTOS_BALAS.json
└── MAPEO_MATERIALES_NUEVOS_TACZ.json
```

**Salida:**

```
.minecraft/tacz/tacz_default_gun/data/tacz/recipes/
├── gun/
│   ├── cz75.json
│   ├── m4a1.json
│   └── ... (53 total)
└── ammo/
    ├── 22wmr.json
    ├── 308.json
    └── ... (24 total)
```

---

## 5. Flujo del Script Principal

```
ENTRADA:
  - NUEVOS_COSTOS_ARMAS.json
  - NUEVOS_COSTOS_BALAS.json
  - MAPEO_MATERIALES_NUEVOS_TACZ.json

VALIDACIÓN:
  1. Cargar mapeo de materiales
  2. Verificar materiales soportados
  3. Filtrar materiales no soportados

GENERACIÓN:
  1. Procesar cada arma en tabla_costos
  2. Convertir nombres a etiquetas Forge
  3. Generar estructura de receta JSON
  4. Guardar en /recipes/gun/{id}.json

  5. Procesar cada munición en tabla_costos_municiones
  6. Convertir nombres a etiquetas Forge
  7. Generar estructura de receta JSON
  8. Guardar en /recipes/ammo/{id}.json

SALIDA:
  - 53 archivos JSON de armas
  - 24 archivos JSON de municiones
  - Log de éxito/errores
```

---

## 6. Ejemplo de Actualización Completa

### Antes:

```json
// COSTOS_ARMAS_TACZ.json (original)
{
  "nombre": "M4A1",
  "materiales": {
    "hierro": 38,
    "lapislazuli": 6,
    "madera": 8
  }
}
```

Receta generada:

```json
{
  "materials": [
    { "item": { "tag": "forge:ingots/iron" }, "count": 38 },
    { "item": { "tag": "forge:gems/lapis" }, "count": 6 },
    { "item": { "tag": "minecraft:logs" }, "count": 8 }
  ],
  "result": { "type": "gun", "id": "tacz:m4a1" },
  "type": "tacz:gun_smith_table_crafting"
}
```

---

## 7. Notas Importantes

⚠️ **Etiquetas son case-sensitive**

- `forge:ingots/iron` ≠ `forge:ingots/Iron`

⚠️ **Plural vs Singular**

- `forge:dusts/redstone` (correcto - plural)
- `forge:dust/redstone` (incorrecto - singular)

⚠️ **Minecraft vs Forge**

- Algunos materiales usan tags vanilla: `minecraft:logs`, `minecraft:coal`
- Otros usan tags Forge: `forge:ingots/iron`, `forge:gems/diamond`

⚠️ **Materiales rechazados por el mod**

- El mod valida que TODOS los ingredientes sean válidos
- Si uno falla, toda la receta se rechaza (icono stop)
- Usar SOLO los materiales de la lista soportada

---

## 8. Prueba en Juego

1. Reiniciar Minecraft
2. Abrir mesa de trabajo de TaCZ
3. Ver si todas las armas/municiones muestran sus materiales
4. Si alguno muestra icono de stop: hay material no soportado

---

## 9. Mantenimiento Futuro

Si necesitas volver a actualizar costos:

1. Edita solo los valores en `NUEVOS_COSTOS_ARMAS.json`
2. Verifica que uses SOLO materiales soportados
3. Ejecuta el script `generar_recetas_tacz.py`
4. Reinicia el juego

No necesitas editar manualmente 77 archivos JSON.

---

## Resumen de Cambios Realizados

| Acción                  | Cantidad | Archivo                           |
| ----------------------- | -------- | --------------------------------- |
| Armas actualizadas      | 53       | NUEVOS_COSTOS_ARMAS.json          |
| Municiones actualizadas | 24       | NUEVOS_COSTOS_BALAS.json          |
| Recetas generadas       | 77       | /recipes/                         |
| Etiquetas corregidas    | 3        | MAPEO_MATERIALES_NUEVOS_TACZ.json |
| Materiales removidos    | 4 tipos  | (carbón, 3 bloques)               |
