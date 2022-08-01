import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session['user_id']

    try:
        stocks = db.execute('SELECT symbol, SUM(shares) AS shares, price FROM transactions WHERE user_id = ? GROUP BY symbol HAVING (SUM(shares))>0;', user_id)
        cash = db.execute('SELECT cash FROM users WHERE id = ?',user_id)
        user_cash = cash[0]['cash']

        if not stocks:
            flash('NO stocks owned!')
            redirect('/')


        total_cash_stocks = 0

        for stock in stocks:
            quote = lookup(stock["symbol"])
            stock["name"] = quote["name"]
            stock["price"] = quote["price"]
            stock["total"] = stock["price"] * stock["shares"]
            total_cash_stocks = total_cash_stocks + stock["total"]


        total_cash = total_cash_stocks + user_cash
        return render_template('index.html',total_cash = total_cash , user_cash = user_cash, stocks = stocks)
    except:
        return render_template('index.html')



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':

        shares = int(request.form.get('shares'))
        symbol = request.form.get('symbol')
        stock = lookup(symbol.upper())

        if not symbol:
            return apology('Invalid symbol')

        if stock == None:
            return apology('Not a valid stock')

        if shares < 1:
            return apology('Enter valid number')

        # Current price of stock
        price = stock['price']
        # cost of transcation
        cost = shares * stock['price']
        # Id of current user logged in
        user_id = session['user_id']

        # cash of user
        cash = db.execute('SELECT cash FROM users WHERE id = ?',user_id)
        # get int from dictionary cash
        user_cash = cash[0]['cash']

        if user_cash < cost:
            return apology("Insufficient Funds")

        # Update cash if db
        current_cash = user_cash - cost
        update_cash = db.execute('UPDATE users SET cash = ? WHERE id = ?',current_cash ,user_id, )

        #update
        date = datetime.datetime.now()

        # update transaction
        transaction = db.execute('INSERT INTO transactions (user_id , symbol, shares, price, date) VALUES(?,?,?,?,?)',user_id, stock['symbol'],shares, stock['price'], date)

        flash('Bought!')

        return redirect('/')
    else:
        return render_template('buy.html')




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session['user_id']

    transactions = db.execute('SELECT * FROM transactions WHERE user_id = ?', user_id)

    return render_template('history.html', transactions = transactions)




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'GET':
        return render_template("quote.html")

    else:
        symbol = request.form.get('symbol')

        if not symbol:
            return apology("Enter valid symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology('symbol does not exist')

        flash('Quote')
        return render_template('quoted.html', name = stock['name'], price = stock['price'], symbol = stock['symbol'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method =='POST':
        # define variables
        username = request.form.get("username")
        password = request.form.get('password')
        pwconfirm = request.form.get("confirmation")


        # Ensure username was submitted
        if not username:
            return apology("Must provide username")

        # Ensure password was submitted
        if not password:
            return apology("Must provide password")

        # Check for confirmation
        if not pwconfirm:
            return apology("Must confirm password")

        # Check passwords match
        if pwconfirm != password:
            return apology("Passwords must match")

        pwhash = generate_password_hash(password)
        # add new user to database
        try:
            register = db.execute('INSERT INTO users (username, hash) VALUES (?,?)', username, pwhash)
        except:
            return apology('Username already exists')

        session['user_id'] = register
        flash('registered')
        return redirect('/')
    else:
        return render_template('register.html')

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == 'GET':

        user_id = session['user_id']
        stocks = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol",user_id)

        return render_template('sell.html', symbols = [row['symbol'] for row in stocks])

    else:
        symbol = request.form.get('symbol')
        shares = int(request.form.get('shares'))
        stock = lookup(symbol.upper())

        # Current price of stock
        price = stock['price']
        # cost of transcation
        cost = shares * stock['price']
        # Id of current user logged in
        user_id = session['user_id']

        # cash of user
        cash = db.execute('SELECT cash FROM users WHERE id = ?',user_id)
        # get int from dictionary cash
        user_cash = cash[0]['cash']

        sum_share = db.execute('SELECT shares FROM transactions WHERE user_id = :id AND symbol = :symbol GROUP BY symbol',id = user_id, symbol= symbol)
        users_shares = sum_share[0]['shares']

        if users_shares < shares:
            return apology('Insufficient shares')

        # Update cash if db
        current_cash = user_cash + cost
        update_cash = db.execute('UPDATE users SET cash = ? WHERE id = ?',current_cash ,user_id, )


        #update
        date = datetime.datetime.now()

        # update transaction
        transaction = db.execute('INSERT INTO transactions (user_id , symbol, shares, price, date) VALUES(?,?,?,?,?)',user_id, stock['symbol'],(-1)*shares, stock['price'], date)



        flash('Sold!')
    return redirect('/')
