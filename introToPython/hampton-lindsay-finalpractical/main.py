import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        response_page = Page()
        
        if self.request.GET:
          self.form_submission_status = True
          response_page.form_data(self.request.GET)
        else:
          self.form_submission_status = False

        self.response.write(response_page.view(self.form_submission_status))

class Page(object):
    def __init__(self):
        self.page_title = "Guessing Game"

    def view(self, form_submitted):
        if form_submitted:
            self.full_name = self.form_data['full_name']
            self.num1 = self.form_data['num1']
            self.num2 = self.form_data['num2']
            self.num3 = self.form_data['num3']
            self.num = [self.num1, self.num2, self.num3]
            self.lowest = min(self.num)
            self.template = open('confirmation.html','r').read().format(**locals())
        else:
            self.template = open('index.html','r').read().format(**locals())
        return self.template

    def form_data(self, data):
      self.form_data = data

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)