TITLES = {
    "privacy_policy": "Privacy Policy",
    "employment_agreement": "Employment Agreement",
    "nda": "Non-Disclosure Agreement",
    "incident_response": "Incident Response Plan",
    "terms_and_conditions": "Terms & Conditions",
}


def render_document(document_type, business_name, owner, address, effective_date):
    title = TITLES[document_type]
    intro = f
    bodies = {
        "privacy_policy": ,
        "employment_agreement": ,
        "nda": ,
        "incident_response": ,
        "terms_and_conditions": ,
    }
    return title, intro + bodies[document_type].strip() + "\n"
