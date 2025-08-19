from datetime import time

SUN_SIGN_DATES = [
    ("Capricorn",  (12, 22), (1, 19)),
    ("Aquarius",   (1, 20),  (2, 18)),
    ("Pisces",     (2, 19),  (3, 20)),
    ("Aries",      (3, 21),  (4, 19)),
    ("Taurus",     (4, 20),  (5, 20)),
    ("Gemini",     (5, 21),  (6, 20)),
    ("Cancer",     (6, 21),  (7, 22)),
    ("Leo",        (7, 23),  (8, 22)),
    ("Virgo",      (8, 23),  (9, 22)),
    ("Libra",      (9, 23),  (10, 22)),
    ("Scorpio",    (10, 23), (11, 21)),
    ("Sagittarius",(11, 22), (12, 21)),
]

ELEMENT = {
    "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
    "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
    "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
    "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
}

SIGN_TRAITS = {
    "Aries": "bold, action-oriented, thrives on challenge",
    "Taurus": "steady, practical, values security and comfort",
    "Gemini": "curious, communicative, adaptable",
    "Cancer": "intuitive, protective, home-and-family focused",
    "Leo": "confident, expressive, leadership-driven",
    "Virgo": "analytical, detail-oriented, service-minded",
    "Libra": "harmonizing, diplomatic, partnership-focused",
    "Scorpio": "intense, strategic, transformation-seeking",
    "Sagittarius": "adventurous, philosophical, freedom-loving",
    "Capricorn": "disciplined, ambitious, long-term planner",
    "Aquarius": "original, humanitarian, systems-thinker",
    "Pisces": "empathetic, imaginative, spiritually attuned"
}

def get_sun_sign(month: int, day: int) -> str:
    for sign, start, end in SUN_SIGN_DATES:
        if start[0] == 12 and month == 12 and day >= start[1]:  
            return sign
        if start[0] == 12 and month == 1 and day <= end[1]:     
            return sign
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Capricorn"  

def life_path_number(year: int, month: int, day: int) -> int:
    """Reduce yyyy+mm+dd digits to a single digit 1-9 (treat 11 and 22 as master numbers)"""
    digits = [int(d) for d in f"{year:04d}{month:02d}{day:02d}"]
    total = sum(digits)
    def reduce(n):
        while n not in (11, 22) and n > 9:
            n = sum(int(d) for d in str(n))
        return n
    return reduce(total)

def ascendant_bucket(t: time) -> str:
    """Toy approximation: map time-of-day to a 'rising sign' bucket for flavor"""
    hour = t.hour
    buckets = [
        (0, 2, "Water Rising"), (2, 4, "Air Rising"), (4, 6, "Earth Rising"),
        (6, 8, "Fire Rising"), (8, 10, "Water Rising"), (10, 12, "Air Rising"),
        (12, 14, "Earth Rising"), (14, 16, "Fire Rising"), (16, 18, "Water Rising"),
        (18, 20, "Air Rising"), (20, 22, "Earth Rising"), (22, 24, "Fire Rising")
    ]
    for start, end, label in buckets:
        if start <= hour < end:
            return label
    return "Air Rising"

def reading_from_profile(name: str, sun_sign: str, life_path: int, ascendant: str) -> str:
    element = ELEMENT.get(sun_sign, "Unknown")
    trait = SIGN_TRAITS.get(sun_sign, "balanced and versatile")
    
    themes = {
        1: "leadership and self-direction",
        2: "partnerships and diplomacy",
        3: "creativity and communication",
        4: "structure and long-term foundations",
        5: "change, travel, and flexibility",
        6: "service, family, and responsibility",
        7: "analysis, learning, and inner growth",
        8: "career ambition, money, and influence",
        9: "purpose, completion, and giving back",
        11: "intuition and inspiring others",
        22: "big-build projects with real-world impact"
    }
    theme = themes.get(life_path, "balance across multiple areas")
    lines = [
        f"**{name}**, your chart headline blends **{sun_sign} ({element})** energy — {trait} — with a life path focused on **{theme}**.",
        f"Your ascendant flavor reads as **{ascendant}**, suggesting how others first perceive you and how you start new cycles.",
        f"Over the next 3–6 months, lean into strengths of **{element}** energy while watching its shadow sides:"
    ]
    shadows = {
        "Fire": "impulsivity and burnout — pace bold moves with recovery days.",
        "Earth": "over-caution and rigidity — schedule experiments to avoid stagnation.",
        "Air": "overthinking and scattered focus — set weekly constraints to ship.",
        "Water": "emotional over-absorption — use boundaries and grounding rituals."
    }
    lines.append(f"- Potential pitfalls: {shadows.get(element, 'stay balanced and reflective.')}")
    lines.append("**Practical nudge:** pick one monthly intention and tie it to a measurable habit.")
    return "\n\n".join(lines)

def answer_question(q: str, sun_sign: str, life_path: int, ascendant: str) -> str:
    q_lower = q.lower()
    topic = "general"
    for key in ["career", "job", "work", "promotion", "internship"]:
        if key in q_lower: topic = "career"
    for key in ["love", "relationship", "marriage", "partner", "crush"]:
        if key in q_lower: topic = "love"
    for key in ["money", "finance", "wealth", "income", "salary"]:
        if key in q_lower: topic = "money"
    for key in ["health", "fitness", "wellness", "sleep"]:
        if key in q_lower: topic = "health"
    for key in ["study", "exam", "university", "college", "learning"]:
        if key in q_lower: topic = "study"
    for key in ["travel", "move", "relocate", "trip"]:
        if key in q_lower: topic = "travel"

    
    element = {
        "Aries":"Fire","Leo":"Fire","Sagittarius":"Fire",
        "Taurus":"Earth","Virgo":"Earth","Capricorn":"Earth",
        "Gemini":"Air","Libra":"Air","Aquarius":"Air",
        "Cancer":"Water","Scorpio":"Water","Pisces":"Water"
    }.get(sun_sign, "Air")

    base = {
        "career": "Map the next 90 days: 1 flagship goal, 3 milestones, weekly deliverables.",
        "love": "Name your non‑negotiables and one growth edge; practice weekly check‑ins.",
        "money": "Follow 50/30/20 for 8 weeks; automate transfers every payday.",
        "health": "Anchor sleep and hydration first; add 2× strength sessions weekly.",
        "study": "Use 50‑minute deep‑work blocks with active recall and spaced repetition.",
        "travel": "Commit to dates, budget, and 3‑place shortlist; book one anchor reservation.",
        "general": "Write a one‑page plan: priorities, constraints, and the first next action."
    }[topic]

    element_twist = {
        "Fire": "Act fast, then iterate — momentum is your ally.",
        "Earth": "Favor steady cadence over big leaps — systems beat sprints.",
        "Air": "Reduce options; decide by explicit criteria to avoid analysis loops.",
        "Water": "Check in with energy and mood — protect recovery time."
    }[element]

    life_hint = {
        1: "Take the lead on decisions; own the outcome.",
        2: "Co‑create with a partner or mentor; feedback is fuel.",
        3: "Communicate progress publicly; make it playful.",
        4: "Build checklists and routines; consistency compounds.",
        5: "Keep optionality; test small before committing big.",
        6: "Balance duty with self‑care; avoid over‑giving.",
        7: "Track inputs and learnings; reflection boosts returns.",
        8: "Negotiate; quantify value — numbers tell the story.",
        9: "Align with purpose; finish lingering tasks.",
        11: "Trust first instincts; capture insights immediately.",
        22: "Think in roadmaps; ship tangible increments."
    }.get(life_path, "Return to your monthly intention; cut one distraction.")

    return f"**Topic:** {topic.title()}\n\n{base}\n\n{element_twist}  \n{life_hint}\n\n*Note: This is a light, rule‑based reading for demo purposes.*"
