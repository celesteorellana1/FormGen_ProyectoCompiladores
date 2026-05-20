// Generado automáticamente por FormGem — fuente: registro_empleado.fg
// Formulario: RegistroEmpleado
// NO editar manualmente — regenerar desde el .fg

// ── Validadores genéricos reutilizables ─────────────────────

function _validar_helper_1(value) {
  const v = (value ?? "").toString().trim();
  if (!v) return "Este campo es requerido";
  return null;
}

// ── Validaciones por campo ───────────────────────────────────

const validaciones = {

  // Sección: DatosPersonales
  nombre(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if ((value ?? "").toString().trim().length < 3) return "Mínimo 3 caracteres";
    if ((value ?? "").toString().trim().length > 80) return "Máximo 80 caracteres";
    return null;
  },

  email(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    const _emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (value && !_emailRx.test(value)) return "Ingresa un correo electrónico válido";
    return null;
  },

};

// ── Handler de envío ─────────────────────────────────────────

async function enviarRegistroEmpleado(datos) {
  // Validar todos los campos antes de enviar
  const errores = {};
  for (const [campo, validar] of Object.entries(validaciones)) {
    const error = validar(datos[campo] ?? "");
    if (error) errores[campo] = error;
  }
  if (Object.keys(errores).length > 0) {
    return { ok: false, errores };
  }

  try {
    const respuesta = await fetch("/api/empleados", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });

    if (respuesta.ok) {
      console.info("Empleado registrado correctamente");
      window.location.href = "/lista";
      return { ok: true };
    } else {
      return { ok: false, mensaje: "mostrar mensaje" };
    }
  } catch (err) {
    return { ok: false, mensaje: "mostrar mensaje: " + err.message };
  }
}

// ── Activación en tiempo real (debounce 300ms) ───────────────

function _debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

function activarRegistroEmpleado(formElement) {
  if (!formElement) { console.error("Elemento de formulario no encontrado"); return; }

  for (const [campo, validar] of Object.entries(validaciones)) {
    const input = formElement.querySelector(`[name="${campo}"]`);
    if (!input) continue;

    const mostrarError = _debounce((valor) => {
      const error = validar(valor);
      let msgEl = formElement.querySelector(`[data-error="${campo}"]`);
      if (!msgEl) {
        msgEl = document.createElement("span");
        msgEl.dataset.error = campo;
        msgEl.style.color = "red";
        msgEl.style.fontSize = "0.85em";
        input.insertAdjacentElement('afterend', msgEl);
      }
      msgEl.textContent = error ?? "";
    }, 300);

    input.addEventListener("input", (e) => mostrarError(e.target.value));
    input.addEventListener("blur",  (e) => mostrarError(e.target.value));
  }

  formElement.addEventListener("submit", async (e) => {
    e.preventDefault();
    const datos = Object.fromEntries(new FormData(formElement));
    const resultado = await enviarRegistroEmpleado(datos);
    if (!resultado.ok && resultado.errores) {
      for (const [campo, msg] of Object.entries(resultado.errores)) {
        let msgEl = formElement.querySelector(`[data-error="${campo}"]`);
        if (!msgEl) {
          const input = formElement.querySelector(`[name="${campo}"]`);
          if (!input) continue;
          msgEl = document.createElement("span");
          msgEl.dataset.error = campo;
          msgEl.style.color = "red";
          msgEl.style.fontSize = "0.85em";
          input.insertAdjacentElement('afterend', msgEl);
        }
        msgEl.textContent = msg;
      }
    }
  });
}

// ── Exportación ──────────────────────────────────────────────
if (typeof module !== "undefined") {
  module.exports = { validaciones, enviarRegistroEmpleado, activarRegistroEmpleado };
}
