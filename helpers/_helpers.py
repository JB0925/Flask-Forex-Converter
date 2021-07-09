def create_results(session_dict, from_, to, amount, symbol, converted):
    categories = 'from to amount symbol converted'.split()
    args = [from_, to, amount, symbol, converted]
    
    if len(args) != 5:
        raise ValueError ('Must have no more or less than five values!') 
    
    for i in range(len(categories)):
        session_dict[categories[i]] = args[i]
    
    return session_dict


def clear_results(session_dict):
    keys = ['from to amount symbol converted']
    for i in range(len(keys)):
        if session_dict.get(keys[i]):
            session_dict[keys[i]] = ''
    
    return


def get_symbol_and_conversion_amount(fromval, toval, amount, symbols, currency):
    symbol = symbols.get_symbol(toval)
    conversion = currency.get_rate(fromval, toval)
    converted_amount = round(float(conversion) * float(amount), 2)
    return symbol, converted_amount


def get_currency_form_values(form):
    fromval = form['from'].upper().strip()
    toval = form['to'].upper().strip()
    amount = float(form['amount'])

    return fromval, toval, amount
