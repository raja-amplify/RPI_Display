#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hi.py
#  
#  Copyright 2022 root <root@raja-IdeaPad-Gaming-3-15IMH05>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def main():
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      #'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('example.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=800, debug=True)
