function _validar_helper_1(value) {
  const v = (value ?? "").toString().trim();
  if (!v) return "Este campo es requerido";
  return null;
}

const validaciones = {

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

  telefono(value) {
    if ((value ?? "").toString().trim().length < 8) return "Mínimo 8 caracteres";
    if ((value ?? "").toString().trim().length > 15) return "Máximo 15 caracteres";
    return null;
  },

  categoria(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    const _opts = ["Hardware", "Software", "Red", "Cuenta", "Otro"];
    if (value && !_opts.includes(value)) return "Opción no válida";
    return null;
  },

  prioridad(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    const _opts = ["Baja", "Media", "Alta", "Crítica"];
    if (value && !_opts.includes(value)) return "Opción no válida";
    return null;
  },

  fecha_incidente(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if (value && isNaN(Date.parse(value))) return "Fecha inválida";
    return null;
  },

  descripcion(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if ((value ?? "").toString().trim().length < 20) return "Mínimo 20 caracteres";
    if ((value ?? "").toString().trim().length > 1000) return "Máximo 1000 caracteres";
    return null;
  },

  numero_equipo(value) {
    if ((value ?? "").toString().trim().length > 50) return "Máximo 50 caracteres";
    return null;
  },

  acepta_seguimiento(value) {
    return null;
  },

};

async function enviarSoporteTecnico(datos) {
  const errores = {};
  for (const [campo, validar] of Object.entries(validaciones)) {
    const error = validar(datos[campo] ?? "");
    if (error) errores[campo] = error;
  }
  if (Object.keys(errores).length > 0) {
    return { ok: false, errores };
  }

  try {
    const respuesta = await fetch("http://127.0.0.1:8000/api/soporte/tickets", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });

    if (respuesta.ok) {
      console.info("Tu ticket fue enviado correctamente");
      window.location.href = "/soporte/confirmacion";
      return { ok: true };
    } else {
      return { ok: false, mensaje: "Error al enviar el ticket, intenta de nuevo" };
    }
  } catch (err) {
    return { ok: false, mensaje: "Error al enviar el ticket, intenta de nuevo: " + err.message };
  }
}

function _debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

function activarSoporteTecnico(formElement) {
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
    const resultado = await enviarSoporteTecnico(datos);
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

if (typeof module !== "undefined") {
  module.exports = { validaciones, enviarSoporteTecnico, activarSoporteTecnico };
}
