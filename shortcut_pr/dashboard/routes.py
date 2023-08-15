from flask import Blueprint, render_template, request, flash, redirect, url_for
from shortcut_pr import col
import json
from bson import json_util
dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard', methods=['GET'])
def show_dashboard():
    income = col.aggregate([{
        '$group':
            {
                "_id": {'type': '$type'},
                "count": {'$sum': '$amount'}

            }
    }
    ])
    income_docs = []
    for doc in income:
        income_docs.append(doc['count'])
    #income_dumps = json.dumps(income_docs)
    # print(income_dumps)
    return render_template('chart.html', income_vs_expenses=income_docs)
