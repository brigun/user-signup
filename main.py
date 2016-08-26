#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
#define regular expressions for validations
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
"""
# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

signup_form = """
<form method="post">
    <table>
        <tbody>
            <tr>
                <td>
                    <label>Username</label>
                </td>
                <td>
                    <input type="text" name="username" value="%(username)s">
                </td>
                <div class="error" >
                    %(error)s
                </div>
            </tr>
            <tr>
                <td>
                    <label>Password</label>
                </td>
                <td>
                    <input type="password" name="password" value="%(password)s">
                </td>
                <div class="error">
                    %(error)s

                </div>
            </tr>
            <tr>
                <td><label>Verify Password</label>
                </td>
                <td>
                    <input type="password" name="verify" value="%(verify)s">
                </td>
                <div class="error">
                    %(error)s

                </div>
            </tr>
            <tr>
                <td>
                    <label>E-mail (<em>optional</em>)</label>
                </td>
                <td>
                    <input type="text" name="email" value="%(email)s">
                </td>
                <div class="error">
                    %(error)s

                </div>
            </tr>
        </tbody>
    </table>
<br>
<input type="submit">
</form>
"""

welcome_form = """
<h2>Welcome, %s!</h2>
Congratulations on signing up!
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        error = self.request.get("error")
        username = self.request.get("username")
        verify = self.request.get("verify")
        email = self.request.get("email")




        #self.write_form()
        self.response.write(page_header + signup_form + page_footer)

    def post(self):

        #check for valid Username
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        if  not valid_username(username):

            error = "That is not a valid username"
            #self.write_form(username, error)

        elif  not valid_password(password):

            error = "That is not a valid password"
            #self.write_form(password, error)

        elif verify != password:

            error = "That password does not match"
            #self.write_form(verify, error)

        elif not valid_email(email):

            error = "That is not a valid e-mail"
            #self.write_form(email, error)

        else:

            response = page_header + welcome_form % (username) + page_footer
            #self.response.write(response)

        self.response.write(page_header + signup_form % {"error": error,
                                                        "username": username,
                                                        "verify": verify,
                                                        "password": password,
                                                        "email": email
                                                         } + page_footer)

    #def write_form(self, username="", password="", verify="", email="", error=""):
        #self.response.write(page_header + signup_form % {"error": error,
                                                        #"username": username,
                                                        #"verify": verify,
                                                        #"password": password,
                                                        #"email": email
                                                         #} + page_footer)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
