# ⚙️ Compatibilidades & Conflictos Conocidos

---

## 🔴 Conflictos Críticos

### 1. Epic Fight + Armas de Otros Mods

**Problema:**

- Epic Fight proporciona animaciones de combate
- Armas de otros mods no tienen compatibilidad integrada
- Resultado: El personaje se ve "congelado" al atacar con armas no-compatibles

**Mods Afectados:**

- ⚔️ MrCrayfish's Gun Mod
- ⚔️ Epic Knights (armaduras, armas medievales)
- ⚔️ Otros mods que agreguen armas

**Soluciones:**

1. Buscar **"Epic Fight Compatible Datapacks"** en CurseForge
2. Buscar **"Epic Fight Addons"** para cada mod de armas
3. Si no encuentran, **considerar sacrificar Epic Fight**

**Recomendación:**
→ Antes de confirmar épica, validar que existan datapacks para armas medievales + fusiles

---

### 2. The Roads More Travelled - Alto Rendimiento

**Problema:**

- Este mod genera caminos con cada paso del jugador
- Crea chunks continuamente para registrar rutas
- Alto impacto en lag en servidores compartidos

**Mitigación:**

- Solo agregar si el servidor tiene recursos (8GB+ RAM)
- Validar con 4+ jugadores en stress test
- Considerar desactivar en zonas de alto tráfico

**Recomendación:**
→ **Esperar a probar en servidor antes de confirmar**

---

### 3. Sodium está Rechazado

**Alternativa:** Embeddium

| Aspecto     | Sodium        | Embeddium |
| ----------- | ------------- | --------- |
| FPS         | +++++         | ++++      |
| Estabilidad | ⚠️ Conflictos | ✅ Seguro |
| Status      | ❌ No usar    | ✅ Usar   |

---

## 🟡 Dependencias Críticas

### Magia

```
┌─ Iron's Spells 'n Spellbooks ─┐
│                              │
├─ Ars 'n Spells (puente) ◄────┤
│                              │
└─ Ars Nouveau ─────────────────┘

Orden de instalación:
1. Ars Nouveau (base)
2. Ars 'n Spells (conector)
3. Iron's Spells (complemento)
```

### Mochilas

```
Sophisticated Backpacks
     ↓ requiere
Sophisticated Core
```

### Construcción

```
Litematica (moldes)
     ↓ pide
Framework (Fabric)
   o MaLiLib (Forge)
```

---

## 🟢 Grupos Compatibles

### Sistem de Magia Unificado

✅ **Iron's Spells 'n Spellbooks**  
✅ **Ars Nouveau** (+ Ars 'n Spells bridge)  
✅ **Apotheosis** (encantamientos RPG)  
→ Juntos crean un sistema mágico profundo

### Combate Épico

✅ **Epic Fight** (animaciones)  
✅ **Epic Knights** (armaduras/armas) + datapack  
✅ **MrCrayfish's Gun** (fusiles) + datapack  
✅ **Mutant Monsters** (enemigos épicos)  
✅ **Mowzie's Mobs** (boss fights)  
→ Requiere datapacks de compatibilidad

### Cocina & Lifestyle

✅ **Farmer's Delight**  
✅ **Alex's Delight** (complemento)  
✅ **[Let's Do] Vinery** (bebidas)  
→ Sistema de comida expandido

### Dimensiones Temáticas

✅ **Terralith** (biomas overworld)  
✅ **Incendium** (Nether mejorado)  
✅ **Nullscape** (End mejorado)  
✅ **Alex's Caves** (biomas especiales)  
✅ **Deeper and Darker** (dimensión Warden)  
✅ **The Aether** (cielo)  
✅ **Twilight Forest** (bosque crepuscular)  
→ Mundo expansivo y diverso

---

## 🔧 Configuraciones Recomendadas

### Instalación Básica (Core)

```
Rendimiento:
- Embeddium
- Better FPS - Render Distance

Utilidad:
- JEI
- JER
- Mouse Tweaks
- Item Highlighter

Mods/Gameplay:
- Waystones (teleporte)
- Sophisticated Backpacks
- Litematica
```

### Instalación Intermedia (+Magia & Combate)

```
(Básica +)

Magia:
- Iron's Spells 'n Spellbooks
- Ars Nouveau
- Ars 'n Spells

Combate:
- Epic Fight
- Epic Knights + datapacks
- Mowzie's Mobs

Mundo:
- Terralith
- Incendium
- Alex's Caves
```

### Instalación Completa (Todo)

```
(Intermedia +)

Todas las dimensiones
Todas las decoraciones
Sound Physics + Simple Voice Chat
Medieval Music
Todos los mobs/animales
```

---

## 🚨 Validaciones Antes de Launch

- [ ] **Epic Fight datapacks** → Descargar y validar armas
- [ ] **The Roads More Travelled** → Stress test con 4+ jugadores
- [ ] **Versiones exactas** → Todos en 1.20.1 o 1.21.1
- [ ] **Loader** → ¿Forge, NeoForge o Fabric?
- [ ] **RAM servidor** → ¿Soporta todas las dimensiones?
- [ ] **Conflictos de puertos** → Voice chat (Simple Voice)
- [ ] **Permisos de construcción** → Si hay mods de claim/protección

---

**Última actualización:** 2026-07-09
