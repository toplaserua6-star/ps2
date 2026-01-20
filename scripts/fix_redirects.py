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
            inputs[i].setAttribute('value', base + '/thank-you.html');
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
    content = re.sub(r'name="redirect" value="[^"]*"', 'name="redirect" value=""', content)

    # 2. Remove conflicting wpcf7mailsent script
    # Matches the specific script block with flexible whitespace
    conflict_pattern = re.compile(r'<script>\s*document\.addEventListener\(\s*[\'"]wpcf7mailsent[\'"]\s*,[\s\S]*?<\/script>', re.DOTALL)
    content, count = re.subn(conflict_pattern, '', content)
    if count > 0:
        print(f"  Removed {count} conflicting script instance(s).")

    # 3. Update or Append new script
    # Check if we already have the OLD version of our script (without setAttribute) or just check if we have ANY version
    # If we have the old version, replace it.
    old_snippet_marker = 'var base = window.location.origin;'
    
    if old_snippet_marker in content:
        # We need to replace the existing script block with the new one
        # Assuming the old script block looks roughly like the one we inserted
        # Use a regex to find the script containing our marker
        my_script_pattern = re.compile(r'<script>\s*document\.addEventListener\("DOMContentLoaded",\s*function\(\)\s*\{\s*var base = window\.location\.origin;[\s\S]*?<\/script>', re.DOTALL)
        content = re.sub(my_script_pattern, snippet.strip(), content)
        print("  Updated existing fix script.")
    else:
        # Append new script if it doesn't exist
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
print("Processing index.html")
process_file("index.html")

# Process subdirectories
for d in dirs:
    path = os.path.join(d, "index.html")
    print(f"Processing {path}")
    process_file(path)
