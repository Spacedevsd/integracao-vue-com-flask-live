from flask import Blueprint, render_template, jsonify, request

from . import db
from .schema import ContactSchema
from .models import Contact

contact = Blueprint("contact", __name__)

@contact.route("/")
def base():
    return render_template("base.html")


@contact.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        name = request.get_json()["name"]

        contact = Contact(name=name)
        db.session.add(contact)
        db.session.commit()

        schema = ContactSchema().dump(contact)
        return jsonify(schema)

    contacts = Contact.query.all()
    schema = ContactSchema(many=True).dump(contacts)
    
    return jsonify(schema)