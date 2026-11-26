def clean_text(text):
   if not text:
      return ""
   text = " ".join(text.split())
   return text
   
     