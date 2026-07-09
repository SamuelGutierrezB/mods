# ⚡ Análisis de Rendimiento & Optimizaciones

---

## 📊 Categorías de Impacto

| Impacto | Símbolo | Descripción | Ejemplos |
|---------|---------|-------------|----------|
| **Muy Bajo** | ▽ | -0 a 5% FPS | Tools, UI, Decoración |
| **Bajo** | ▼ | -5 a 10% FPS | Biomas, mobs simples |
| **Medio** | ◆ | -10 a 20% FPS | Magia, dimensiones, LOD |
| **Alto** | ▲ | -20 a 35% FPS | Shaders, múltiples dimensiones |
| **Crítico** | ▲▲ | -35%+ FPS | The Roads More Travelled, renderizado extremo |

---

## 🔍 Mods Evaluados

### ▽ IMPACTO MUY BAJO (No preocupar)

```
✅ JEI / JER                    - Solo UI
✅ Mouse Tweaks                 - Input
✅ Item Highlighter             - Partículas mínimas
✅ Litematica                   - Solo visualización
✅ OpenBlocks Elevator          - Bloques simples
✅ Medieval Music               - Audio
✅ Iron Furnaces Enhanced       - Máquinas simples
```

### ▼ IMPACTO BAJO (Aceptable)

```
✅ Alex's Caves                 - Biomas generativos
✅ Terralith                    - Generación vanilla mejorada
✅ Incendium                    - Nether mejorado
✅ Nullscape                    - End mejorado
✅ The Aether                   - Dimensión limpia
✅ Twilight Forest              - Dimensión estable
✅ Deeper and Darker            - Dimensión pequeña
✅ The Undergarden              - Dimensión pequeña
✅ Alex's Mobs                  - Mobs renderizados
✅ Mowzie's Mobs                - Boss fights (3 mobs)
✅ Sound Physics Remastered     - Cálculos de audio
✅ Simple Voice Chat            - Red, no GPU
✅ Xaero's Minimap              - UI
✅ Waystones                    - Blocks simples
```

### ◆ IMPACTO MEDIO (Monitorear)

```
⚠️ Epic Fight                   - Animaciones complejas
⚠️ Ars Nouveau                  - Efectos de magia
⚠️ Iron's Spells 'n Spellbooks - Efectos de hechizos
⚠️ Apotheosis                   - Procesamiento de encantamientos
⚠️ YUNG's Better Dungeons       - Generación de estructuras
⚠️ Mutant Monsters              - Mobs complejos
⚠️ Supplementaries              - Bloques decorativos
⚠️ Journey Map                  - Renderizado de mapa
⚠️ Distant Horizons             - LOD (Level of Detail)
```

### ▲ IMPACTO ALTO (Validar antes de agregar)

```
❌ Oculus                       - Solo si usan shaders
❌ Better FPS (Render Distance)- Depende de settings
❌ Embeddium                    - Optimización (puede ayudar)
```

### ▲▲ IMPACTO CRÍTICO (No agregar sin stress test)

```
🔴 The Roads More Travelled     - Genera chunks constantemente
   └─ Requiere 8GB+ RAM en servidor
   └─ Stress test obligatorio con 4+ jugadores
```

---

## 🎯 Recomendaciones Estratégicas

### Para Servidores con 4GB RAM

**Incluir:**
- ✅ Rendimiento: Embeddium, Better FPS
- ✅ Core: JEI, Waystones, Backpacks
- ✅ Biomas: Terralith (solo overworld)
- ✅ 1-2 dimensiones pequeñas
- ✅ Magia: Sistema completo (bajo impacto)

**Excluir:**
- ❌ The Roads More Travelled
- ❌ Distant Horizons
- ❌ Múltiples dimensiones generativas

**FPS esperado:** 40-60 (4 jugadores)

---

### Para Servidores con 8GB+ RAM

**Incluir:**
- ✅ Todo lo anterior
- ✅ The Roads More Travelled (con validación)
- ✅ Todas las dimensiones
- ✅ Epic Fight + completo

**FPS esperado:** 60+ (4 jugadores)

---

## 📈 Curva de Rendimiento

```
Config Mínima          Config Media           Config Máxima
(Core)                 (Magia + 3D)           (Todas las features)
│                      │                      │
├─ JEI                 ├─ (Anterior)         ├─ (Anterior)
├─ Backpacks           ├─ Terralith          ├─ The Roads Travelled ⚠️
├─ Waystones           ├─ 2 dimensiones      ├─ Todas las dimensiones
├─ Embeddium           ├─ Epic Fight         ├─ Epic Fight + Knights
│                      ├─ Magia completa     ├─ Shaders (Oculus)
FPS: 80+               │                      │
                       ├─ Sound Physics      ├─ Voice Chat
                       │                      ├─ Distant Horizons
                       FPS: 50-70            │
                                             FPS: 30-60
```

---

## 🛠️ Optimizaciones en Juego

### Configuración de Cliente (Cada Jugador)

```
✅ Graphics: Fast
✅ Render Distance: 8-12 chunks
✅ Simulation Distance: 8 chunks
✅ Particles: Decreased
✅ Biome Blend: Off
✅ Smooth Lighting: Min
✅ V-Sync: On (60 FPS cap)
```

### Configuración de Servidor

```yaml
# server.properties
simulation-distance=10
view-distance=10
difficulty=1 (Easy/Normal)
online-mode=false (para pruebas)

# bukkit.yml (si es Bukkit/Paper)
spawn-limits:
  monsters: 70
  animals: 10
```

### Comandos Útiles

```bash
# Monitorear entidades
/forceload query

# Ver chunks cargados
/debug report

# Limpiar entidades
/kill @e[type=!player]
```

---

## 📋 Checklist Pre-Launch

- [ ] **Medir FPS base** sin mods
- [ ] **Agregar mods core** (JEI, Embeddium) → Medir
- [ ] **Agregar magia** (Ars + Iron) → Medir
- [ ] **Agregar combate** (Epic Fight) → Medir
- [ ] **Agregar 3 dimensiones** → Medir
- [ ] **Agregar The Roads** → Stress test 4+ jugadores
- [ ] **Publicar resultados** en RENDIMIENTO.md
- [ ] **Ajustar si FPS < 30** (remover mods secundarios)

---

## 📝 Template para Reportar Rendimiento

```
Fecha: YYYY-MM-DD
Servidor: [RAM disponible]
Mods totales: [N]

Config:
- Render Distance: 12
- Simulation Distance: 10
- Jugadores simultáneos: 4

Resultados:
- FPS promedio (idle): XX
- FPS promedio (explorando): XX
- FPS promedio (combate): XX
- Lag spikes: [Sí/No] @ ubicación X,Y,Z

Notas:
- The Roads Travelled generó XX chunks en 1 hora
- Multiplayer performance stable ✓/✗
- Recomendación: [Optimizar / Agregar más mods / Remover]
```

---

**Última actualización:** 2026-07-09  
**Responsable:** Team Rendimiento
