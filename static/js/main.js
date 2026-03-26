const form = document.getElementById("contactForm");
const status = document.getElementById("formStatus");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  status.textContent = "Sending...";
  status.style.color = "#666";

  const data = {
    name: form.name.value.trim(),
    email: form.email.value.trim(),
    message: form.message.value.trim(),
  };

  try {
    const res = await fetch("/contact", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await res.json();
    if (res.ok) {
      status.style.color = "#2c6e49";
      status.textContent = "✅ Message sent! Thank you.";
      form.reset();
    } else {
      status.style.color = "#c0392b";
      status.textContent = "❌ " + (result.error || "Something went wrong.");
    }
  } catch (err) {
    status.style.color = "#c0392b";
    status.textContent = "❌ Could not reach the server.";
  }
});

// Certificate click → open modal
document.querySelectorAll(".cert-img-wrap img").forEach((img) => {
  img.addEventListener("click", () => {
    const modal = document.getElementById("imgModal");
    const modalImg = document.getElementById("modalImg");

    if (modal && modalImg) {
      modal.style.display = "flex";
      modalImg.src = img.src;
    }
  });
});

// Click anywhere to close
const modal = document.getElementById("imgModal");

if (modal) {
  modal.addEventListener("click", () => {
    modal.style.display = "none";
  });
}
