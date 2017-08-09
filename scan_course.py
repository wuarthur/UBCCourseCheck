import requests
from bs4 import BeautifulSoup


URLs = []
class _CourseUrl:
    def __init__(self, dept, course, section):
        self.url= 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + dept +'&course='+ course+ '&section=' + section

URLs.append(_CourseUrl('AANB','500','KRS'))
URLs.append(_CourseUrl('GEM','520','101'))

for course in URLs:
    r = requests.get(course.url)
    html_doc = r.text
    if 'Total Seats Remaining:</td><td align=&#39;left&#39;><strong>0' not in html_doc:
        print 'total'
    if 'General Seats Remaining:</td><td align=&#39;left&#39;><strong>0' not in html_doc:
        print 'general'
    if 'Restricted Seats Remaining*:</td><td align=&#39;left&#39;><strong>0' not in html_doc:
        print 'restricted'
