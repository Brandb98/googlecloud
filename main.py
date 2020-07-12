from google.cloud import ndb
client = ndb.Client()
client

# from flask import Flask, render_template, request
# from google.cloud import ndb
# from contact_model import Contact

# app = Flask(__name__)
# client = ndb.Client(project="hiwold")

# @app.route(r'/', methods=['GET'])
# def contact_book():
#     return render_template('contact_book.html')

# @app.route(r'/add', methods=['GET', 'POST'])
# def add_contact():

#     if request.form:
#         with client.context():
#             contact = Contact(
#                             name=request.form.get('name'),
#                             phone=request.form.get('phone'),
#                             email=request.form.get('email')
#                         )
#         contact.put()

#     return render_template('add_contact.html')

# if __name__ == '__main__':
#     app.run()