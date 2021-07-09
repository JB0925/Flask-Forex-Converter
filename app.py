import os
import sys
topdir = os.path.join(os.path.dirname(__file__), '.')
sys.path.append(topdir)

from flask import Flask, render_template, url_for, redirect, request, flash, session
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from decouple import config

from helpers import _helpers

cur = CurrencyRates()
symbols = CurrencyCodes()

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    """The conversion page of the app. A GET request will render the
       main template. A successful POST request will redirect to the
       results page, where all data will be displayed. An unsuccessful
       POST request gets redirected to the home page, where an error
       message will be displayed."""
    if request.method == 'GET':
        return render_template('home.html')
    
    try:
        form = request.form
        
        fromval, toval, amount = _helpers.get_currency_form_values(form)
        symbol, converted_amount = _helpers.get_symbol_and_conversion_amount(fromval,
                                    toval,amount,symbols, cur)
        _helpers.create_results(session, fromval, toval, amount, symbol, converted_amount)

        return redirect(url_for('results'))

    except RatesNotAvailableError:
        flash('Sorry, one or both of your currencies could not be found.', 'error')
        _helpers.clear_results(session)
        return redirect(url_for('home'))


@app.route('/results')
def results():
    """This page simply displays the results of a successful
       conversion between two currencies."""
    return render_template('result.html', results=session)