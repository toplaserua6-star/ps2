import os
import re

# Include root directory and all subdirectories
root_dir = "."
dirs = ["contacts", "diagnosticheskiy-priem", "konsultatsiya-psihologa-online", 
        "lechenie-bessonnitsy", "lechenie-depressii", "lechenie-nevroza", 
        "lechenie-panicheskih-atak", "lechenie-ptsr", "lechenie-vygoraniya", 
        "liczenziya", "nashi-filialy", "service"]

snippet = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        var base = window.location.origin;
        var inputs = document.querySelectorAll('input[name="redirect"]');
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].value = base + '/thank-you.html';
        }
    });
</script>
"""

def process_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return

    with open(filepath, "r") as f:
        content = f.read()

    original_content = content

    # 1. Clear hardcoded redirect value
    # Matches name="redirect" value="..." and replaces value with empty string
    content = re.sub(r'name="redirect" value="[^"]*"', 'name="redirect" value=""', content)

    # 2. Append script if not present
    if "var base = window.location.origin;" not in content:
        if "</body>" in content:
            content = content.replace("</body>", snippet + "\n</body>")
        else:
            print(f"Warning: No </body> tag in {filepath}")

    if content != original_content:
        print(f"Updating {filepath}")
        with open(filepath, "w") as f:
            f.write(content)
    else:
        print(f"No changes needed for {filepath}")

# Process root index.html
process_file("index.html")

# Process subdirectories
for d in dirs:
    path = os.path.join(d, "index.html")
    process_file(path)
