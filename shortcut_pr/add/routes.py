from flask import Blueprint, render_template, request, flash, redirect, url_for
from shortcut_pr import col
from shortcut_pr.add.forms import UserInputForm
add = Blueprint('add', __name__)


@add.route('/add', methods=['GET', 'POST'])
def add_expense():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = {
            'type': form.type.data,
            'category': form.category.data,
            'amount': form.amount.data
        }
        col.insert_one(entry)
        flash('Data added successfuly', 'success')
        return redirect(url_for('main.home'))
    return render_template('add.html', title='Add expenses', form=form)
