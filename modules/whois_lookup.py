import whois

def lookup_domain(domain):
    try:
        data = whois.whois(domain)
        return {
            "domain_name": data.domain_name,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "name_servers": data.name_servers,
            "emails": data.emails,
        }
    except Exception as e:
        return {"error": str(e)}
