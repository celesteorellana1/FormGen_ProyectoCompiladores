// Generado por FormGem - fuente: formulario_completo.fg
// Formulario: RegistroCompleto

function _validar_helper_1(value) {
  const v = (value ?? "").toString().trim();
  if (!v) return "Este campo es requerido";
  return null;
}

const validaciones = {

  // Seccion: DatosPersonales
  nombre(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if ((value ?? "").toString().trim().length < 3) return "Minimo 3 caracteres";
    if ((value ?? "").toString().trim().length > 80) return "Maximo 80 caracteres";
    return null;
  },

  email(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    const _emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (value && !_emailRx.test(value)) return "Ingresa un correo electronico valido";
    return null;
  },

  password(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if ((value ?? "").toString().trim().length < 8) return "Minimo 8 caracteres";
    return null;
  },

  fecha_nacimiento(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    if (value && isNaN(Date.parse(value))) return "Fecha invalida";
    return null;
  },

  // Seccion: DatosLaborales
  puesto(value) {
    { const _e = _validar_helper_1(value); if (_e) return _e; }
    const _opts = ["Desarrollador", "Diseñador", "Analista", "Gerente"];
    if (value && !_opts.includes(value)) return "Opcion no valida";
    return null;
  },

  salario(value) {
    if (Number(value) < 1000.0) return "El valor minimo es 1000.0";
    if (Number(value) > 99999.99) return "El valor maximo es 99999.99";
    return null;
  },

  edad(value) {
    if (Number(value) < 18.0) return "El valor minimo es 18.0";
    if (Number(value) > 65.0) return "El valor maximo es 65.0";
    return null;
  },

  descripcion(value) {
    if ((value ?? "").toString().trim().length > 500) return "Maximo 500 caracteres";
    return null;
  },

  // Seccion: Configuracion
  activo(value) {
    return null;
  },

  readonly_field(value) {
    return null;
  },

  interno(value) {
    return null;
  },

};

async function enviarRegistroCompleto(datos) {
  const errores = {};
  for (const [campo, validar] of Object.entries(validaciones)) {
    const error = validar(datos[campo] ?? "");
    if (error) errores[campo] = error;
  }
  if (Object.keys(errores).length > 0) {
    return { ok: false, errores };
  }

  console.warn("No se definio bloque on_submit en el formulario.");
  return { ok: false, mensaje: "Sin accion de envio configurada" };
}

function _debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

function activarRegistroCompleto(formElement) {
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
    const resultado = await enviarRegistroCompleto(datos);
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
  module.exports = { validaciones, enviarRegistroCompleto, activarRegistroCompleto };
}
