# Create a dictionary with some sample data
person = {
    "name": "nuur",
    "birthdate": "January 1, 2004",
    "address": {
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}

# Generate an HTML output using the data
html = f"<h1>{person['name']}</h1>\n"
html += f"<p>Birthdate: {person['birthdate']}</p>\n"
html += f"<p>Address:</p>\n"
html += f"<ul>\n"
html += f"  <li>{person['address']['street']}</li>\n"
html += f"  <li>{person['address']['city']}, {person['address']['state']} {person['address']['zip']}</li>\n"
html += f"</ul>\n"

# Print the HTML output
print(html)