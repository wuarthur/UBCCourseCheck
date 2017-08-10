import requests
# from bs4 import BeautifulSoup
import SMPT
import pickle

# Each Course Object will have a CourseUrl Object
# Course Object: Dept, Course Number, Section, SeatingType, CourseUrl Object, ListOfUsers
# Course Url: Dept, Course, Section

class _CourseUrl:
    def __init__(self, dept, course, section):
        self.url= 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + dept +'&course='+ course+ '&section=' + section
        self.name = dept + ' ' + course + ' ' + section

class _Course:
    def __init__(self, dept, course, section, SeatingType, CourseUrl):
        self.name = dept + course + section + SeatingType
        self.dept = dept
        self.course = course
        self.section = section
        self.SeatingType = SeatingType
        self.CourseUrl = CourseUrl
        self.users = []

with open('users.pickle', 'rb') as handle:
    users_dict = pickle.load(handle)

Courses = []

for key, value in users_dict.iteritems():
    user_email = value[0]
    course_list = value[1]
    for course in course_list:
        course_vals = course.split(',')
        course_dept = course_vals[0]
        course_number = course_vals[1]
        course_section = course_vals[2]
        course_SeatingType = course_vals[3]

        #create course url object
        course_url = _CourseUrl(course_dept,course_number,course_section)

        #create course object
        new_course = _Course(course_dept,course_number,course_section,course_SeatingType,course_url)

        #First check whether course is empty
        if not Courses:
            # If courses list is empty, create new course and add to list
            new_course.users.append(user_email)
            Courses.append(new_course)
        # Else go through list of courses to see if there is a duplicate
        else:
            # See if course object already exists, if it exists append user email to course
            course_exists = False
            for course in Courses:
                if course.name == new_course.name:
                    course.users.append(user_email)
                    course_exists = True

            # Otherwise, append the users email to the newly created course list and add the course to courses
            if not course_exists:
                new_course.users.append(user_email)
                Courses.append(new_course)

#Entries = open('Courses.txt').read().split('\n')
#for line in Entries:
#    data=line.split(',')
#    #print line
#    #Users.append(data[0])


#URLs = []
#URLs.append(_CourseUrl('AANB','500','KRS'))
#URLs.append(_CourseUrl('GEM','520','101'))
for course in Courses:
    r = requests.get(course.CourseUrl.url)
    html_doc = r.text
    if 'Total Seats Remaining:</td><td align=&#39;left&#39;><strong>0' not in html_doc:
        #SMPT._sendEmailToUsers(course.users,course.name)
        print 'sent Email'
    if 'General Seats Remaining:</td><td align=&#39;left&#39;><strong>0' not in html_doc:
        print 'general'

