const API_BASE = "http://localhost:8000/api";

const form = document.querySelector(".contact-form");
const btn = form.querySelector(".contact-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const payload = {
    name: form.name.value.trim(),
    email: form.email.value.trim(),
    message: form.message.value.trim(),
  };

  if (!payload.name || !payload.email || !payload.message) return;

  btn.disabled = true;
  btn.textContent = "Sending...";

  try {
    const res = await fetch(`${API_BASE}/contact/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      btn.textContent = "Sent!";
      form.reset();
    } else {
      btn.textContent = "Something went wrong";
    }
  } catch {
    btn.textContent = "Could not reach server";
  } finally {
    setTimeout(() => {
      btn.textContent = "Send Message";
      btn.disabled = false;
    }, 3000);
  }
});
