import os
import re

dirs = ["contacts", "diagnosticheskiy-priem", "konsultatsiya-psihologa-online", 
        "lechenie-bessonnitsy", "lechenie-depressii", "lechenie-nevroza", 
        "lechenie-panicheskih-atak", "lechenie-ptsr", "lechenie-vygoraniya", 
        "liczenziya", "nashi-filialy", "service"]

# Simple form template (Name + Phone)
simple_template = """<div class="wpcf7 no-js" id="GENERIC_ID" lang="ru-RU" dir="ltr">
<form action="https://api.web3forms.com/submit" method="POST" class="wpcf7-form init">
<input type="hidden" name="access_key" value="78c1b7d4-b1b3-4c53-831c-0f1649313701">
<input type="hidden" name="redirect" value="https://uae.igordar.com/thank-you.html">
<input type="hidden" name="subject" value="Заявка с внутренней страницы">
<span class="wpcf7-form-control-wrap" data-name="text-173"><input size="40" maxlength="400" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" aria-required="true" aria-invalid="false" placeholder="Имя" value="" type="text" name="name" required /></span>
<span class="wpcf7-form-control-wrap" data-name="text-904"><input size="40" maxlength="400" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required phone-mask" aria-required="true" aria-invalid="false" placeholder="+7" value="" type="text" name="phone" required /></span>
<button>Запись на консультацию</button>
</form>
</div>"""

# Extended form template (Name + Phone + Message)
extended_template = """<div class="wpcf7 no-js" id="GENERIC_ID" lang="ru-RU" dir="ltr">
<form action="https://api.web3forms.com/submit" method="POST" class="wpcf7-form init">
<input type="hidden" name="access_key" value="78c1b7d4-b1b3-4c53-831c-0f1649313701">
<input type="hidden" name="redirect" value="https://uae.igordar.com/thank-you.html">
<input type="hidden" name="subject" value="Заявка с внутренней страницы (с сообщением)">
<span class="wpcf7-form-control-wrap" data-name="text-369"><input size="40" maxlength="400" class="wpcf7-form-control wpcf7-text" aria-invalid="false" placeholder="Ваше имя" value="" type="text" name="name" /></span>
<span class="wpcf7-form-control-wrap" data-name="tel-556"><input size="40" maxlength="400" class="wpcf7-form-control wpcf7-tel wpcf7-validates-as-required wpcf7-text wpcf7-validates-as-tel phone-mask" aria-required="true" aria-invalid="false" placeholder="+7" value="" type="tel" name="phone" required /></span>
<span class="wpcf7-form-control-wrap" data-name="textarea-223"><textarea cols="40" rows="10" maxlength="2000" class="wpcf7-form-control wpcf7-textarea wpcf7-validates-as-required" aria-required="true" aria-invalid="false" placeholder="Опишите Вашу проблему (необязательно)" name="message"></textarea></span>
   <div class="bottom">
    <button class="btn-blue">Запись на консультацию</button>
    <div class="info">Отправляя заявку, вы соглашаетесь с условиями политики конфиденциальности и обработку персональных данных</div>
   </div>
</form>
</div>"""

for d in dirs:
    path = os.path.join(d, "index.html")
    if os.path.exists(path):
        print(f"Processing {path}")
        with open(path, "r") as f:
            content = f.read()
        
        # Regex to match the entire div wrapping the form
        # We assume the div looks like <div class="wpcf7 no-js" id="..."> ... </div>
        # And contains a <form> inside.
        pattern = re.compile(r'<div class="wpcf7 no-js" id="([^"]+)"[^>]*>.*?<form action="[^"]+" method="post" class="wpcf7-form init"[^>]*>.*?</form>\s*</div>', re.DOTALL)
        
        def replace_callback(match):
            full_match = match.group(0)
            original_id = match.group(1)
            
            if "textarea-223" in full_match:
                print(f"  Replacing Extended Form {original_id}")
                return extended_template.replace("GENERIC_ID", original_id)
            else:
                print(f"  Replacing Simple Form {original_id}")
                return simple_template.replace("GENERIC_ID", original_id)
        
        new_content, count = re.subn(pattern, replace_callback, content)
        
        if count > 0:
            print(f"  Replaced {count} forms.")
            with open(path, "w") as f:
                f.write(new_content)
        else:
            print("  No forms found matching pattern.")
