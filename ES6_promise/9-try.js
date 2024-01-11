export default function guardrail(mathFunction) {
  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (x) {
    return [`${x.name}: ${x.message}`, 'Guardrail was processed'];
  }
}
