from flask import Flask, render_template, request, jsonify
import ipaddress
import uuid
import random
from faker import Faker  # To generate random User Agents and Lorem Ipsum Text

app = Flask(__name__)

fake = Faker()  # Create a Faker instance

def generate_ip(ip_version):
    if ip_version == 'IPv4':
        return str(ipaddress.IPv4Address(random.getrandbits(32)))
    else:  # IPv6
        return str(ipaddress.IPv6Address(random.getrandbits(128)))

def generate_uuid():
    return str(uuid.uuid4())

def generate_credit_card(card_type):
    if card_type == 'Visa':
        number = '4' + ''.join(random.choice('0123456789') for _ in range(15))
    elif card_type == 'Mastercard':
        number = '5' + str(random.randint(1, 5)) + ''.join(random.choice('0123456789') for _ in range(14))
    else:
        return None
    expiry = f"{random.randint(1, 12):02d}/{random.randint(22, 30):02d}"
    cvv = ''.join(random.choice('0123456789') for _ in range(3))
    return f"{number} | {expiry} | {cvv}"

def generate_user_agent():
    return fake.user_agent()

def generate_lorem_ipsum():
    return fake.text()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    item_type = data.get('item_type')
    count = min(int(data.get('count', 1)), 100)
    
    if item_type == 'IPv4':
        items = [generate_ip('IPv4') for _ in range(count)]
    elif item_type == 'IPv6':
        items = [generate_ip('IPv6') for _ in range(count)]
    elif item_type == 'UUID':
        items = [generate_uuid() for _ in range(count)]
    elif item_type == 'Visa':
        items = [generate_credit_card('Visa') for _ in range(count)]
    elif item_type == 'Mastercard':
        items = [generate_credit_card('Mastercard') for _ in range(count)]
    elif item_type == 'UserAgent':
        items = [generate_user_agent() for _ in range(count)]
    elif item_type == 'LoremIpsum':
        items = [generate_lorem_ipsum() for _ in range(count)]
    else:
        return jsonify({'error': 'Invalid item type'}), 400
    
    return jsonify({'generated_items': items})

if __name__ == '__main__':
    app.run(debug=True)
