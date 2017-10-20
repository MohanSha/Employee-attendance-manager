import yagmail
yag = yagmail.SMTP("mohansha@qubecinema.com", "")

html_msg = """Dear Mohan, <br><br>
            Your attendance information from 21st AUG to 20th SEP 2017."""
yag.send("mohansha@qubecinema.com", "Test Mail", html_msg)
print "Email Sent"