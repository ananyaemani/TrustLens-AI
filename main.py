import customtkinter as ctk
from risk_engine import calculate_risk
from mentor import get_advice

# ----------------------------
# App Settings
# ----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("TrustLens AI - Digital Safety Mentor")
app.geometry("1200x900")

# ----------------------------
# Functions
# ----------------------------

def analyze():

    text = textbox.get("1.0", "end").strip()

    if not text:
        return

    score, risks = calculate_risk(text)

    advice = get_advice(score)

    if score <= 2:
        threat = "LOW 🟢"
    elif score <= 5:
        threat = "MEDIUM 🟡"
    else:
        threat = "HIGH 🔴"

    risk_label.configure(
        text=f"Risk Score: {score}/10"
    )

    threat_label.configure(
        text=f"Threat Level: {threat}"
    )

    progress.set(score / 10)

    risks_box.delete("1.0", "end")

    if risks:
        for risk in risks:
            risks_box.insert("end", f"• {risk}\n")
    else:
        risks_box.insert("end", "No major risks detected.")

    advice_box.delete("1.0", "end")
    advice_box.insert("end", advice)


def clear_all():

    textbox.delete("1.0", "end")

    risk_label.configure(
        text="Risk Score: --/10"
    )

    threat_label.configure(
        text="Threat Level: UNKNOWN"
    )

    progress.set(0)

    risks_box.delete("1.0", "end")
    advice_box.delete("1.0", "end")


# ----------------------------
# Header
# ----------------------------

title = ctk.CTkLabel(
    app,
    text="🛡 TrustLens AI",
    font=("Arial", 36, "bold")
)
title.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(
    app,
    text="Analyze messages for scams, manipulation, grooming and cyberbullying",
    font=("Arial", 16)
)
subtitle.pack(pady=(0, 20))

# ----------------------------
# Input Section
# ----------------------------

input_label = ctk.CTkLabel(
    app,
    text="Paste Message / Chat",
    font=("Arial", 24, "bold")
)
input_label.pack()

textbox = ctk.CTkTextbox(
    app,
    width=950,
    height=220,
    font=("Arial", 15)
)
textbox.pack(pady=15)

# ----------------------------
# Buttons
# ----------------------------

button_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
button_frame.pack(pady=10)

analyze_btn = ctk.CTkButton(
    button_frame,
    text="🔍 Analyze Message",
    width=220,
    height=45,
    command=analyze
)
analyze_btn.grid(row=0, column=0, padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=150,
    height=45,
    command=clear_all
)
clear_btn.grid(row=0, column=1, padx=10)

# ----------------------------
# Results Frame
# ----------------------------

result_frame = ctk.CTkFrame(
    app,
    width=1100,
    height=400
)
result_frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

risk_label = ctk.CTkLabel(
    result_frame,
    text="Risk Score: --/10",
    font=("Arial", 28, "bold")
)
risk_label.pack(pady=(20, 5))

threat_label = ctk.CTkLabel(
    result_frame,
    text="Threat Level: UNKNOWN",
    font=("Arial", 22)
)
threat_label.pack()

progress = ctk.CTkProgressBar(
    result_frame,
    width=500
)
progress.pack(pady=15)
progress.set(0)

# ----------------------------
# Detected Risks
# ----------------------------

risks_title = ctk.CTkLabel(
    result_frame,
    text="Detected Risks",
    font=("Arial", 18, "bold")
)
risks_title.pack()

risks_box = ctk.CTkTextbox(
    result_frame,
    width=800,
    height=100,
    font=("Arial", 14)
)
risks_box.pack(pady=10)

# ----------------------------
# Mentor Advice
# ----------------------------

advice_title = ctk.CTkLabel(
    result_frame,
    text="Digital Mentor Advice",
    font=("Arial", 18, "bold")
)
advice_title.pack()

advice_box = ctk.CTkTextbox(
    result_frame,
    width=800,
    height=120,
    font=("Arial", 14)
)
advice_box.pack(pady=10)

# ----------------------------
# Run App
# ----------------------------

app.mainloop()