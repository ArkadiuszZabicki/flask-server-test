from flask import Blueprint, render_template, request, flash, redirect, url_for
from shortcut_pr import col
from bson.objectid import ObjectId
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    entries = col.find()

    return render_template('index.html', title='Home page', entries=entries)


@main.route('/delete/<entry_id>')
def delete(entry_id):
    col.delete_one({"_id": ObjectId(entry_id)})
    flash('Deletion was successful', 'success')
    return redirect(url_for('main.home'))
