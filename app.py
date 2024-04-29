from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize messages list
messages = []

@app.route('/')
def index():
    if messages: ''
    return render_template('index.html', messages=messages) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/library')
def library():
    return render_template('library.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')

@app.route('/request')
def request_page():
    return render_template('request_page.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission here, if needed
    # Redirect to the thank you page
   return render_template('thankyou.html')

@app.route('/')
def delivery_form():
    return render_template('delivery_details.html')

@app.route('/submit_delivery', methods=['POST'])
def submit_delivery():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    # Here you can add code to store the details or perform any other actions
    return render_template('thank_you.html', name=name)

@app.route('/delivery_details', methods=['POST'])
def delivery_details():
    # Handle delivery details form submission here
    return render_template('delivery_details.html')

@app.route('/thank_you')
def thank_you():
    return "<h1>Thank You for Your Order!</h1>"



@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']

    # Add user message to messages list
    messages.append({'sender': 'user', 'content': user_input})

    # Check for the clear command
    if "bye" in user_input.lower():
        clear_conversation()
        bot_response = ""

    # Add bot response (replace with your chatbot logic)
    bot_response = get_bot_response(user_input)
    messages.append({'sender': 'bot', 'content': bot_response})

    return render_template('index.html', messages=messages)

def get_bot_response(user_input):
    #to check if a a specific response has been provided
    response_provided = False
    # Replace this with your actual chatbot logic or API call
    if "hello" in user_input.lower():
        bot_response = "Hi there! How can I help you?"
        response_provided = True
    elif "how are you" in user_input.lower():
        bot_response = "I'm very well. Thank you."
        response_provided = True
    elif "working hours" in user_input.lower():
        bot_response = "I'm available round the clock"
        response_provided = True
    elif "book request" in user_input.lower():
        bot_response = "Yes, you can. Kindly fill the contact form with the title, author's name, genre and why we should stock the book"
        response_provided = True
    elif "do you offer gift wrapping services" in user_input.lower():
        bot_response = "Of course, we do. Fill the contact form to let us know if you need it"
        response_provided = True
    elif "open hours" in user_input.lower():
        bot_response = "I'm available round the clock but our store opens by 9:00 am to 7:00 pm from Monday to Friday. We open from 10:00 am to 6:00 pm on Saturday. We are closed on Sunday."
        response_provided = True    
    #elif "books" in user_input.lower():
     #   bot_response = "Please proceed to library"
      #  response_provided =True
    elif "purchase" in user_input.lower():
        bot_response = "Please proceed to the purchase page"
        response_provided = True
    elif "store address" in user_input.lower():
        bot_response = "Please proceed to the contact us page"
        response_provided = True
    elif "help me find a book" in user_input.lower():
        bot_response = "Certainly! Can I have the title?"
        response_provided = True
    elif "can you recommend a book" in user_input.lower():
        bot_response = "Certainly! What do you fancy? Some adventure maybe? romance? mystery? self-help? leadership? horror? thriller? fan-fiction?"
        response_provided = True
    elif "adventure" in user_input.lower():
       bot_response = "Good choice. Here are some of our newly-stocked adventure novels: Lord of the Rings, Prince Caspian, Wizard of Oz, Peter Pan, Into Nerdaland, All Hail Sire."
       response_provided = True
    elif "what is your return policy for books" in user_input.lower():
        bot_response = "In order to be refunded, books must be returned in good condition within ten working days"
        response_provided = True
    elif "do you host author events or book signing" in user_input.lower():
        bot_response = "We do but it is strictly contract-based"
        response_provided = True
    elif "Is it possible to sell my used books to your store" in user_input.lower():
        bot_response = "Of course but it will be bought at a cheaper rate"
        response_provided = True
    elif "do you have a children's section" in user_input.lower():
        bot_response = "No, we do not"
        response_provided = True
    elif "online orders" in user_input.lower():
        bot_response = "Yes, you can place orders online. Kindly use the contact form"
        response_provided = True
    elif "what payment methods do you accept" in user_input.lower():
        bot_response = "We accept cash, cards and online transfers"
        response_provided = True
    elif "do you offer discounts" in user_input.lower():
        bot_response = "Yes, we offer discounts for educators and bulk purchases"
        response_provided = True
    elif "how often do you receive new book shipments" in user_input.lower():
        bot_response = "We receive new book shipments forthnightly"
        response_provided = True
    elif "do you have a loyalty program" in user_input.lower():
        bot_response = "Yes, we have a 'loyalty points' system that can be redeemed for rewards"
        response_provided = True
    elif "what genres of books do you carry" in user_input.lower():
        bot_response = "We have every genre you fancy. If you don't find ypur preferred genre, kindly fill the contact form so we can stock it."
        response_provided = True
    elif "pre-order" in user_input.lower():
        bot_response = "Sure. Fill in the details on the purchase page and leave us a message using the contact form"
        response_provided = True
    elif "do you offer both new and used books" in user_input.lower():
        bot_response = "Yes, we do. Used books are sold at a slightly cheaper rate"
        response_provided = True
    elif "thanks" in user_input.lower():
        bot_response = "Anytime"
        response_provided = True
    elif "thank you" in user_input.lower():
        bot_response = "Sure. Happy reading!"
        response_provided = True
    if not response_provided:
        bot_response = "Need help?"
    return bot_response

    

def clear_conversation():
    global messages
    messages = [] 

if __name__ == '__main__':
    app.run(debug=True)
