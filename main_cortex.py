if msg["type"] == "template_mutation":
    template_db.integrate(msg["template"])