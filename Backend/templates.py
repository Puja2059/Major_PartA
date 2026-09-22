TITLES = {
    "privacy_policy": "Privacy Policy",
    "employment_agreement": "Employment Agreement",
    "nda": "Non-Disclosure Agreement",
    "incident_response": "Incident Response Plan",
    "terms_and_conditions": "Terms & Conditions",
}


def render_document(document_type, business_name, owner, address, effective_date):
    title = TITLES[document_type]
    intro = (
        f"Draft document: {title}\n"
        f"Business: {business_name}\n"
        f"Owner: {owner}\n"
        f"Address: {address}\n"
        f"Effective date: {effective_date}\n\n"
    )

    bodies = {
        "privacy_policy": (
            "This Privacy Policy explains how the business collects, uses, stores, and protects personal information. "
            "The business will collect only the information needed for lawful operations and will apply reasonable security "
            "controls to protect it. Individuals may request access to their data, corrections, or deletion where legally "
            "applicable. This draft should be reviewed with the business's actual data practices before use."
        ),
        "employment_agreement": (
            "This Employment Agreement sets out the duties, compensation, working arrangements, leave, confidentiality, "
            "and termination terms for the employee. The employee agrees to follow company policies, perform assigned work "
            "with reasonable care, and protect confidential information. The business will provide lawful pay, working hours, "
            "and notice periods in accordance with applicable law and internal policy. Review all terms with legal counsel before use."
        ),
        "nda": (
            "This Non-Disclosure Agreement requires each party to keep confidential information private and to use it only for "
            "the agreed business purpose. Confidential information includes business plans, technical information, customer data, "
            "and other sensitive details disclosed in connection with the relationship. The receiving party must protect such "
            "information with reasonable safeguards and return or destroy it upon request or termination."
        ),
        "incident_response": (
            "This Incident Response Plan defines how the business will detect, contain, assess, communicate, and recover from "
            "security incidents. The response team will record the event, evaluate business impact, decide on containment steps, "
            "and notify relevant stakeholders where required. The business should review and test the plan regularly to keep it effective."
        ),
        "terms_and_conditions": (
            "These terms apply to the use of the business's goods or services. Customers agree to provide accurate information, "
            "use the service lawfully, and comply with any posted policies. The business may update these terms as needed, while "
            "continuing to protect customer data and clarify service responsibilities. This draft should be reviewed against the "
            "specific product, jurisdiction, and commercial arrangement before use."
        ),
    }
    return title, intro + bodies[document_type].strip() + "\n"
