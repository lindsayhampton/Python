import webapp2
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        if self.request.GET:
            p.title = "I love vodka"
            my_name = self.request.GET['name']
            my_age = self.request.GET['age']
            #self.response.write(my_name + " " + my_age)
            p.show_output(my_name, my_age)
            html = p.print_out()
            self.response.write(html)
        else:
            p.title = "I LOVE BEER"
            html = p.print_out()
            self.response.write(html)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
class Page(object):
    def __init__(self):
        self.title = ""
        self.css = "css/styles.css"
        self.head = '''
<!DOCTYPE>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css}" />
    </head>
    <body>
'''
        self.body = '''
<form method="GET">
    <label>What is your name?</label>
    <input type="text" name="name">
    <label>What is your age?</label>
    <input type="text" name="age">
    <button type="submit">Click</button>
</form>
'''
        self.close = '''
    </body>
</html>
'''
    def print_out(self):
        all = (self.head + self.body + self.close).format(**locals())
        return all
    def show_output(self,n,a):
        self.n = n
        self.a = a
        self.body = '''
<p>Your name is, {self.n}.</p>
<p>Your age is, {self.a}.</p>
'''