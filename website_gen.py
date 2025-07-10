def generate_website(title, content):
    return f"""<!DOCTYPE html>
<html>
<head><title>{title}</title></head>
<body><h1>{title}</h1><p>{content}</p></body>
</html>"""
