import streamlit as st

st.set_page_config(page_title="Campus Care MVP", page_icon="🚗", layout="centered")


def render_styles(theme_mode: str):
    if theme_mode == "Dark":
        bg_color = "#0b1220"
        text_color = "#e5e7eb"
        card_bg = "#111827"
        card_border = "#374151"
        shadow = "0 2px 10px rgba(0, 0, 0, 0.35)"
    else:
        bg_color = "#f5f8fc"
        text_color = "#111827"
        card_bg = "#ffffff"
        card_border = "#dde6f2"
        shadow = "0 2px 10px rgba(15, 39, 66, 0.08)"

    st.markdown(
        f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');

    :root {{
        --safety-blue: #1f4e79;
        --navy: #0f2742;
        --red: #c1121f;
    }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    h1, h2, h3 {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        letter-spacing: 0.1px;
    }}

    .stApp {{
        background: {bg_color};
        color: {text_color};
    }}

    .hero {{
        background: linear-gradient(135deg, var(--navy), var(--safety-blue));
        color: white;
        padding: 1rem 1.2rem;
        border-radius: 14px;
        margin-bottom: 1rem;
    }}

    .card {{
        background: {card_bg};
        color: {text_color};
        border: 1px solid {card_border};
        border-radius: 12px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.8rem;
        box-shadow: {shadow};
    }}

    .pill {{
        display: inline-block;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
        font-size: 0.78rem;
        border-radius: 999px;
        padding: 0.22rem 0.6rem;
        font-weight: 600;
    }}

    .discount-pill {{
        color: white;
        background: var(--red);
    }}

    .plan-pill {{
        color: #0c4423;
        background: #d1fae5;
    }}

    .rating-pill {{
        color: #7c2d12;
        background: #ffedd5;
    }}

    .severity-red {{
        border-left: 4px solid #dc2626;
    }}
    .severity-orange {{
        border-left: 4px solid #f97316;
    }}
    .severity-yellow {{
        border-left: 4px solid #eab308;
    }}
</style>
        """,
        unsafe_allow_html=True,
    )


car_db = {
    "Toyota": {
        "Corolla": list(range(2010, 2026)),
        "Camry": list(range(2010, 2026)),
        "RAV4": list(range(2012, 2026)),
    },
    "Honda": {
        "Civic": list(range(2010, 2026)),
        "Accord": list(range(2010, 2026)),
        "CR-V": list(range(2012, 2026)),
    },
    "Ford": {
        "Focus": list(range(2010, 2020)),
        "Fusion": list(range(2010, 2021)),
        "Escape": list(range(2012, 2026)),
    },
    "Nissan": {
        "Sentra": list(range(2011, 2026)),
        "Altima": list(range(2010, 2026)),
        "Rogue": list(range(2011, 2026)),
    },
    "Hyundai": {
        "Elantra": list(range(2011, 2026)),
        "Sonata": list(range(2010, 2026)),
        "Tucson": list(range(2012, 2026)),
    },
}

shops = [
    {
        "name": "Northside Auto Clinic",
        "distance": "2.1 mi",
        "rating": 4.8,
        "reviews": 126,
        "student_discount": "15% off labor",
        "payment_plan": "SplitPay available",
        "student_reviews": [
            "Quick brake inspection before my midterm commute.",
            "They explained repairs in plain language, no pressure.",
            "Honored student pricing exactly as listed.",
            "Finished same day and shared photo proof.",
            "Flexible payment options helped me avoid credit card debt.",
        ],
    },
    {
        "name": "Campus Edge Mechanics",
        "distance": "3.5 mi",
        "rating": 4.7,
        "reviews": 84,
        "student_discount": "10% off diagnostics",
        "payment_plan": "0% APR plans",
        "student_reviews": [
            "Great with check-engine diagnostics and code printout.",
            "Loaner shuttle to campus made this stress-free.",
            "Service advisor walked me through what was urgent vs optional.",
            "No surprise fees on my invoice.",
            "They sent text updates while I was in class.",
        ],
    },
    {
        "name": "River City Auto Care",
        "distance": "4.0 mi",
        "rating": 4.6,
        "reviews": 201,
        "student_discount": "Free tire rotation",
        "payment_plan": "Monthly payment plans",
        "student_reviews": [
            "Aligned my wheels and fixed highway vibration.",
            "Super transparent quote with parts and labor separated.",
            "Trusted them for my pre-road-trip safety check.",
            "Front desk was friendly and patient with my questions.",
            "Payment plan approval was fast and easy.",
        ],
    },
]

vin_demo = {
    "1HGCM82633A004352": {
        "owners": "3 previous owners; last registered in IL",
        "recalls": "1 open recall: fuel pump module",
        "value": 4200,
    },
    "1N4AL3AP8FC123456": {
        "owners": "2 previous owners; clean title history",
        "recalls": "No open recalls found",
        "value": 7800,
    },
}

dashboard_lights = [
    {
        "name": "Brake System Warning",
        "icon": "🛑",
        "severity": "Red",
        "meaning": "Brake fluid may be low, parking brake may be engaged, or braking system fault exists.",
        "action": "Stop safely and inspect immediately. Do not drive if braking feels weak.",
    },
    {
        "name": "Oil Pressure",
        "icon": "🛢️",
        "severity": "Red",
        "meaning": "Engine oil pressure is dangerously low.",
        "action": "Shut engine off ASAP. Check oil before restarting.",
    },
    {
        "name": "Check Engine",
        "icon": "🚨",
        "severity": "Orange",
        "meaning": "Engine/emissions system detected a fault code.",
        "action": "If flashing, reduce speed and get immediate service. If steady, schedule diagnosis soon.",
    },
    {
        "name": "ABS",
        "icon": "⭕",
        "severity": "Orange",
        "meaning": "Anti-lock braking assist may be unavailable.",
        "action": "Brakes still work, but avoid hard driving and schedule inspection.",
    },
    {
        "name": "Tire Pressure (TPMS)",
        "icon": "🟡",
        "severity": "Yellow",
        "meaning": "One or more tires are underinflated or sensor battery is weak.",
        "action": "Set tires to door-sticker PSI and recheck in 24 hours.",
    },
    {
        "name": "Low Fuel",
        "icon": "⛽",
        "severity": "Yellow",
        "meaning": "Fuel level is near reserve.",
        "action": "Refuel soon to avoid fuel pump strain.",
    },
]


def run_diagnostic(issue_text: str, symptom: str):
    issue = f"{symptom} {issue_text}".lower()

    data = [
        {
            "keys": ["wont start", "won't start", "dead battery", "battery", "clicking"],
            "checks": [
                "Check battery terminals for corrosion and loose clamps.",
                "Try jump start and check if headlights are dim.",
                "If available, test battery voltage (12.4V+ preferred off).",
            ],
            "next": "If it still will not start, book a charging-system test (battery/alternator/starter).",
            "urgency": "High",
        },
        {
            "keys": ["brake", "grinding", "squeal", "vibration while braking"],
            "checks": [
                "Check brake fluid level in master cylinder reservoir.",
                "Listen whether noise happens only when pedal is pressed.",
                "Look for steering wheel shake during braking from 50+ mph.",
            ],
            "next": "Drive only if needed and schedule service immediately. Brakes are safety-critical.",
            "urgency": "Critical",
        },
        {
            "keys": ["overheat", "hot", "temp", "coolant", "steam"],
            "checks": [
                "When engine is cool, check coolant reservoir level.",
                "Confirm radiator fan turns on after warmup.",
                "Check for sweet smell or visible coolant leaks.",
            ],
            "next": "Stop driving if temp climbs again. Tow if needed to prevent engine damage.",
            "urgency": "Critical",
        },
        {
            "keys": ["rough idle", "misfire", "shaking", "check engine"],
            "checks": [
                "Check gas cap is fully tightened.",
                "Listen for uneven engine rhythm at idle.",
                "Note whether issue is worse during acceleration.",
            ],
            "next": "Get an OBD scan soon and avoid hard acceleration.",
            "urgency": "Medium",
        },
        {
            "keys": ["ac", "no cold air", "heat not working", "blower"],
            "checks": [
                "Confirm cabin fan works on all speed settings.",
                "Set A/C to max and inspect compressor clutch engagement.",
                "Check cabin air filter for heavy blockage.",
            ],
            "next": "Non-safety issue, but schedule HVAC diagnosis for comfort and visibility defogging.",
            "urgency": "Low",
        },
    ]

    for rule in data:
        if any(k in issue for k in rule["keys"]):
            return rule["checks"], rule["next"], rule["urgency"]

    fallback_checks = [
        "Check all fluid levels (oil, coolant, brake fluid).",
        "Inspect tires for pressure and uneven wear.",
        "Note when issue appears: startup, idle, acceleration, braking, or highway speed.",
    ]
    fallback_next = "Monitor short trips only and schedule a professional inspection with symptom notes."
    return fallback_checks, fallback_next, "Medium"


def car_guy_ai_breakdown(issue_text: str):
    issue = issue_text.lower().strip()
    if not issue:
        return None

    likely = ["Minor maintenance item or developing wear issue."]
    checks = ["Record noise/smell/when it happens and avoid hard driving until checked."]
    ask_mechanic = "Can you show me the failed part and rank urgent vs optional repairs?"
    safety = "Watch closely"

    if any(x in issue for x in ["knock", "ticking", "metal", "rod"]):
        likely = [
            "Possible valvetrain or bottom-end engine noise.",
            "Could be low oil level/pressure causing internal wear.",
        ]
        checks = [
            "Check oil level right now before more driving.",
            "If noise rises with RPM, stop driving and arrange inspection.",
        ]
        ask_mechanic = "Can you confirm oil pressure and identify if noise is top-end or bottom-end?"
        safety = "High risk - limit driving"
    elif any(x in issue for x in ["shake", "vibration", "wobble"]):
        likely = [
            "Wheel balance, bent rim, tire wear, or brake rotor runout.",
            "Could also be worn suspension joints.",
        ]
        checks = [
            "Note speed range where vibration starts (example: 55-70 mph).",
            "Inspect tire tread and sidewalls for irregular wear or bulges.",
        ]
        ask_mechanic = "Please check balance, alignment, rotor runout, and front-end play."
        safety = "Medium risk"
    elif any(x in issue for x in ["smoke", "burning", "sweet smell", "coolant smell"]):
        likely = [
            "Fluid leak contacting hot surfaces or coolant system leak.",
            "Could indicate overheating risk.",
        ]
        checks = [
            "Stop and inspect for visible leaks under the car.",
            "Do not open coolant cap when hot.",
        ]
        ask_mechanic = "Can you pressure-test cooling and check for oil/coolant cross-contamination?"
        safety = "High risk - inspect now"
    elif any(x in issue for x in ["hard shift", "slip", "transmission"]):
        likely = [
            "Transmission fluid condition or internal wear concern.",
            "Could be software/adaptation issue on newer models.",
        ]
        checks = [
            "Avoid aggressive acceleration.",
            "Check if shifts worsen when hot vs cold.",
        ]
        ask_mechanic = "Can you scan transmission codes and verify fluid condition/spec?"
        safety = "Medium-High risk"

    return {
        "likely": likely,
        "checks": checks,
        "ask_mechanic": ask_mechanic,
        "safety": safety,
    }


theme_mode = st.segmented_control("Theme", options=["Light", "Dark"], default="Light")
render_styles(theme_mode)

st.markdown(
    """
    <div class="hero">
        <h2 style="margin:0;">Campus Care</h2>
        <p style="margin:0.35rem 0 0 0;">Car maintenance and safety support for commuter students.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

sections = ["Car Diagnostic", "Vouched Mechanics", "VIN Transparency", "Know Your Ride"]
selected = st.radio("Navigate", sections, horizontal=True, label_visibility="collapsed")

if selected == "Car Diagnostic":
    st.subheader("Car Diagnostic Engine")

    make = st.selectbox("Car Make", list(car_db.keys()))
    model = st.selectbox("Car Model", list(car_db[make].keys()))
    year = st.selectbox("Car Year", sorted(car_db[make][model], reverse=True))
    symptom = st.selectbox(
        "Pick a symptom (optional)",
        [
            "General concern",
            "Won't start / dead battery",
            "Brake noise or vibration",
            "Overheating / high temp",
            "Rough idle / check engine",
            "A/C or heater issue",
        ],
    )
    issue = st.text_area(
        "Describe the issue in your own words",
        placeholder="Example: Car shakes between 60-70 mph and feels worse while braking.",
    )

    st.session_state["car_make"] = make
    st.session_state["car_model"] = model
    st.session_state["car_year"] = year
    st.session_state["issue_text"] = issue

    if st.button("Run Diagnostic", type="primary"):
        free_checks, next_steps, urgency = run_diagnostic(issue, symptom)
        st.session_state["free_checks"] = free_checks
        st.session_state["next_steps"] = next_steps
        st.session_state["urgency"] = urgency

    if "free_checks" in st.session_state:
        st.markdown('<div class="card"><b>Free Steps to Check</b><ul>', unsafe_allow_html=True)
        for item in st.session_state["free_checks"]:
            st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="card">
                <b>Recommended Next Steps</b><br/>
                {st.session_state["next_steps"]}<br/><br/>
                <b>Urgency:</b> {st.session_state["urgency"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

elif selected == "Vouched Mechanics":
    st.subheader("Vouched Mechanic Marketplace")
    issue_text = st.session_state.get("issue_text", "I need help diagnosing a car issue.")
    make = st.session_state.get("car_make", "My car")
    model = st.session_state.get("car_model", "")
    year = st.session_state.get("car_year", "")

    prefills = (
        f"Hi, I am a student commuter and need an inquiry for my {year} {make} {model}. "
        f"Issue: {issue_text}"
    )

    for i, shop in enumerate(shops):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"**{shop['name']}**  \n{shop['distance']} away")
        st.markdown(
            f"""
            <span class="pill discount-pill">Student Discount: {shop['student_discount']}</span>
            <span class="pill plan-pill">Payment Plans: {shop['payment_plan']}</span>
            <span class="pill rating-pill">Student Vouched: ⭐ {shop['rating']} ({shop['reviews']} reviews)</span>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("**Recent Student Reviews**")
        for review in shop["student_reviews"]:
            st.write(f"- {review}")

        st.text_area(
            f"Book Inquiry Message ({shop['name']})",
            value=prefills,
            key=f"inquiry_{i}",
            height=95,
        )
        st.button("Book Inquiry", key=f"book_{i}")
        st.markdown("</div>", unsafe_allow_html=True)

elif selected == "VIN Transparency":
    st.subheader("VIN History & Transparency Portal")
    vin = st.text_input("Enter VIN", placeholder="Example: 1HGCM82633A004352")
    repair_cost = st.number_input("Estimated Repair Cost ($)", min_value=0, step=100, value=1200)

    if st.button("Search VIN", type="primary"):
        result = vin_demo.get(vin.strip().upper())
        if result:
            st.markdown(
                f"""
                <div class="card"><b>Ownership History</b><br/>{result['owners']}</div>
                <div class="card"><b>Open Recalls / Safety Alerts</b><br/>{result['recalls']}</div>
                """,
                unsafe_allow_html=True,
            )

            value = result["value"]
            delta = value - repair_cost
            recommendation = (
                "Repair appears financially reasonable."
                if repair_cost <= value * 0.5
                else "Repair may exceed practical value; consider alternatives."
            )
            st.markdown(
                f"""
                <div class="card">
                    <b>Value Calculator</b><br/>
                    Approx vehicle value: ${value:,}<br/>
                    Estimated repair: ${repair_cost:,}<br/>
                    Difference: ${delta:,}<br/>
                    <b>{recommendation}</b>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("No VIN record found in demo dataset. Try: 1HGCM82633A004352")

else:
    st.subheader("Know Your Ride Learning Center")
    tab1, tab2 = st.tabs(["Dashboard Lights Guide", "AI Car-Issue Breakdown"])

    with tab1:
        st.write("Color meanings for warning lights: red = stop now, orange = service soon, yellow = monitor soon.")
        severity = st.selectbox("Filter by severity color", ["All", "Red", "Orange", "Yellow"])

        for light in dashboard_lights:
            if severity != "All" and light["severity"] != severity:
                continue
            css_class = f"severity-{light['severity'].lower()}"
            st.markdown(
                f"""
                <div class="card {css_class}">
                    <b>{light['icon']} {light['name']} ({light['severity']})</b><br/>
                    <b>What it means:</b> {light['meaning']}<br/>
                    <b>What to do:</b> {light['action']}
                </div>
                """,
                unsafe_allow_html=True,
            )

    with tab2:
        issue_lookup = st.text_area(
            "Look up any car issue",
            placeholder="Example: I smell coolant and see white smoke near the hood after traffic.",
        )
        if st.button("Break It Down Like a Car Guy", type="primary"):
            breakdown = car_guy_ai_breakdown(issue_lookup)
            if breakdown is None:
                st.warning("Add a short issue description first.")
            else:
                st.markdown('<div class="card"><b>Likely Causes</b><ul>', unsafe_allow_html=True)
                for item in breakdown["likely"]:
                    st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
                st.markdown("</ul></div>", unsafe_allow_html=True)

                st.markdown('<div class="card"><b>What You Can Check First</b><ul>', unsafe_allow_html=True)
                for item in breakdown["checks"]:
                    st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
                st.markdown("</ul></div>", unsafe_allow_html=True)

                st.markdown(
                    f"""
                    <div class="card">
                        <b>What to Tell the Mechanic</b><br/>
                        {breakdown['ask_mechanic']}<br/><br/>
                        <b>Safety Level:</b> {breakdown['safety']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

st.caption("Campus Care MVP prototype - built for interview demonstration.")
