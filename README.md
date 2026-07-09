# 🎮 Minecraft Java Mods - Documentación Colaborativa

**Servidor temático medieval + magia + dimensiones**

> 📖 Catálogo completo de 59+ mods evaluados y categorizados por la banda.

---

## 📚 Documentación

| Archivo | Contenido |
|---------|----------|
| **[MODS_JAVA_PROPUESTOS.md](MODS_JAVA_PROPUESTOS.md)** | 📋 Catálogo completo (12 categorías, estados, compatibilidades) |
| **[COMPATIBILIDADES.md](COMPATIBILIDADES.md)** | ⚙️ Notas de dependencias y conflictos conocidos |
| **[RENDIMIENTO.md](RENDIMIENTO.md)** | ⚡ Impacto en FPS y optimizaciones |

---

## 🎯 Acceso Rápido

### Busco un mod para...

- **📍 Mapas & Navegación** → Xaero's Minimap, Journey Map
- **⚔️ Combate mejorado** → Epic Fight + Epic Knights + Magia
- **🏗️ Construcción** → Litematica, Sophisticated Backpacks, Chisel Reborn
- **🌍 Mundo más bonito** → Terralith, Incendium, Better Dungeons
- **🐉 Dimensiones nuevas** → Aether, Deeper & Darker, Nullscape, Twilight Forest
- **🎨 Decoración** → Supplementaries, Medieval Music, Sound Physics
- **⚡ Mejor FPS** → Embeddium, Better FPS Render Distance

### Estados de Aprobación

- ✅ **Aprobado** — Listo para agregar
- ⚠️ **Validar** — Pruebas o comparación pendiente
- ❌ **Rechazado** — No recomendado
- 🔗 **Dependencia** — Requerido por otro mod

---

## 🚀 Flujo de Decisión

```
¿Quiero agregar un mod nuevo?
│
├─ ¿Ya está en MODS_JAVA_PROPUESTOS.md?
│  ├─ Sí → Revisa el estado y compatibilidades
│  └─ No → Busca alternativas o propón al equipo
│
├─ ¿Es seguro para el servidor?
│  ├─ Sí (bajo impacto rendimiento) → Agregar
│  └─ No → Marcar como "⚠️ Comparar" o "❌ No"
│
└─ ¿Tiene dependencias?
   ├─ Sí → Validar que estén incluidas
   └─ No → Listo
```

---

## 📝 Formato de Registro

Cuando agregas un mod nuevo a `MODS_JAVA_PROPUESTOS.md`:

```markdown
| **Nombre del Mod** | Versión | Estado | Detalles |
|---|---|---|---|
| **Mi Mod Favorito** | 1.20.1 | ✅ Sí | Breve descripción + por qué lo queremos |
```

---

## ⚠️ Notas Críticas

### Epic Fight
- ✅ Animaciones de combate BUENAS
- 🔴 **Armas de otros mods se ven congeladas sin datapacks**
- 📌 **Solución:** Buscar "Epic Fight Compatible" en CurseForge

### The Roads More Travelled
- 🟡 **ALTO rendimiento** — genera caminos constantemente
- 📌 **Solo si el servidor tiene recursos** (validar antes)

### Sodium vs Embeddium
- ❌ Sodium: Rechazado (conflictos)
- ✅ Embeddium: Alternativa segura para FPS

---

## 🛠️ Próximos Pasos

- [ ] Seleccionar versión objetivo (1.20.1 o 1.21.1)
- [ ] Validar compatibilidad Forge/NeoForge/Fabric
- [ ] Crear pack inicial con mods "core"
- [ ] Testing en staging (4+ jugadores)
- [ ] Documentar conflictos en tiempo real

---

## 📞 Contacto & Decisiones

**Temática aprobada:** Medieval + Magia + Dimensiones  
**Hosting:** Máquina virtual (VTLR u otro)  
**Mantenedor:** SamuelBarona
