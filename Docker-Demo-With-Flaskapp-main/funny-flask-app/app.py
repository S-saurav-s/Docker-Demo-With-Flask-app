from flask import Flask, jsonify, request
import logging
import os
import random
from datetime import datetime

app = Flask(__name__)

# Configure logging with funny format
logging.basicConfig(
    level=logging.INFO,
    format='🤖 %(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
DEBUG = os.getenv('FLASK_DEBUG', False)
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')

# Funny data collections
FUNNY_QUOTES = [
    "I told my computer I needed a break, and now it won't stop sending me Kit-Kat ads.",
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "There are only 10 types of people: those who understand binary and those who don't.",
    "I would tell you a UDP joke, but you might not get it.",
    "Programming is like writing a book... except if you miss a single comma on page 126, the whole thing is trash.",
    "Debugging: Being the detective in a crime movie where you are also the murderer.",
    "99 little bugs in the code, 99 little bugs. Take one down, patch it around, 117 little bugs in the code.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'"
]

FUNNY_FACTS = [
    "Honey never spoils. You could feasibly eat 3000-year-old honey.",
    "A group of flamingos is called a 'flamboyance'.",
    "Bananas are berries, but strawberries aren't.",
    "There are more possible games of chess than atoms in the observable universe.",
    "Octopuses have three hearts and blue blood.",
    "Wombat poop is cube-shaped.",
    "A shrimp's heart is in its head.",
    "The shortest war in history lasted only 38-45 minutes."
]

DAD_JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus!"
]


@app.route('/', methods=['GET'])
def home():
    """Welcome to the Comedy Central of APIs! 🎭"""
    logger.info("Someone entered the comedy club! 🎪")
    return jsonify({
        'message': '🎭 Welcome to the Funniest Flask App Ever! 🎭',
        'tagline': 'Where bugs are features and features are... well, still bugs!',
        'mood': '😂 Laughing Out Loud',
        'timestamp': datetime.utcnow().isoformat(),
        'status': 'Hilariously running!',
        'tip': 'Try /joke, /roast, /dadjoke, /fact, or /insult for maximum giggles!'
    }), 200


@app.route('/health', methods=['GET'])
def health_check():
    """Health check with a twist of humor"""
    logger.info("Doctor checkup time! 👩‍⚕️")
    health_status = random.choice([
        'Healthier than a programmer who uses semicolons correctly',
        'Running smoother than JavaScript... wait, that\'s not saying much',
        'More stable than my Wi-Fi connection',
        'Feeling fresh like a newly initialized array'
    ])
    return jsonify({
        'status': 'Healthy and hilarious! 💪😄',
        'diagnosis': health_status,
        'prescription': 'More coffee and fewer bugs',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/joke', methods=['GET'])
def get_joke():
    """Get a random programming joke"""
    logger.info("Someone needs a laugh! 😂")
    joke = random.choice(FUNNY_QUOTES)
    return jsonify({
        'joke': joke,
        'rating': f"{random.randint(7, 10)}/10 - Certified Knee Slapper! 🦵",
        'warning': 'May cause uncontrollable giggling',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/dadjoke', methods=['GET'])
def get_dad_joke():
    """Get a classic dad joke (warning: may cause eye rolling)"""
    logger.info("Dad has entered the chat! 👨")
    joke = random.choice(DAD_JOKES)
    return jsonify({
        'dad_joke': joke,
        'cringe_level': f"{random.randint(8, 15)}/10",
        'dad_approval': '👨 Two thumbs up from every dad ever',
        'side_effects': 'Eye rolling, groaning, secret smiling',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/fact', methods=['GET'])
def get_funny_fact():
    """Get a weird but true fact"""
    logger.info("Time for some mind-blowing knowledge! 🤯")
    fact = random.choice(FUNNY_FACTS)
    return jsonify({
        'funny_fact': fact,
        'weirdness_scale': f"{random.randint(6, 10)}/10",
        'verified_by': 'The University of Random Wikipedia Deep Dives',
        'use_case': 'Perfect for awkward elevator conversations',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/roast', methods=['GET'])
def roast_user():
    """Get playfully roasted by the API"""
    logger.info("Someone asked to be roasted! 🔥")
    roasts = [
        "You're like a null pointer exception - nobody saw you coming but everyone regrets it! 💥",
        "Your code is so bad, even Stack Overflow closed your questions! 📚",
        "You debug code like you're looking for Waldo in a Where's Waldo book... blindfolded! 👀",
        "Your programming skills are like Internet Explorer - slow, outdated, and everyone's trying to replace you! 🐌",
        "You write code like you're getting paid per line... unfortunately, it's all comments! 📝"
    ]
    roast = random.choice(roasts)
    return jsonify({
        'roast': roast,
        'burn_level': '🔥 Third-degree code burn! 🔥',
        'recovery_tip': 'Apply ice and more Stack Overflow searches',
        'disclaimer': 'All in good fun! You\'re actually awesome! ❤️',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/insult', methods=['GET'])
def shakespeare_insult():
    """Get a sophisticated Shakespearean insult"""
    logger.info("Requesting a classy insult! 🎩")
    adjectives = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish"]
    nouns1 = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming"]
    nouns2 = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole"]
    
    insult = f"Thou {random.choice(adjectives)} {random.choice(nouns1)} {random.choice(nouns2)}!"
    
    return jsonify({
        'shakespearean_insult': insult,
        'translation': 'You magnificent weirdo! (in fancy old English)',
        'class_level': '🎩 Royal Shakespeare Company Approved',
        'best_used': 'At renaissance faires or heated code reviews',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/motivate', methods=['GET'])
def motivate():
    """Get some hilariously motivational advice"""
    logger.info("Someone needs motivation! 💪")
    motivations = [
        "You're like a recursive function - you might not know when to stop, but you'll eventually get there! 🔄",
        "Debugging is just you being a detective in a crime movie where you're also the murderer! 🕵️‍♀️",
        "Remember: Every expert was once a beginner who refused to give up... and had really good Google skills! 🔍",
        "You're not failing, you're just finding 10,000 ways that don't work! Thanks, Edison! 💡",
        "Code like nobody's watching... because they probably aren't, they're all debugging their own stuff! 👀"
    ]
    
    motivation = random.choice(motivations)
    return jsonify({
        'motivation': motivation,
        'confidence_boost': '+9000 Programming Power! ⚡',
        'sponsored_by': 'Coffee and Stack Overflow',
        'side_effects': 'Increased productivity and decreased imposter syndrome',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/info', methods=['GET'])
def app_info():
    """Get hilariously detailed app information"""
    logger.info("Someone wants to know about our comedy goldmine! ℹ️")
    return jsonify({
        'app_name': '🎭 The Comedy Flask API Extravaganza',
        'version': '2.0.LOL',
        'author': 'The Department of Silly APIs',
        'purpose': 'To make developers smile between debugging sessions',
        'environment': 'Comedy Central' if not DEBUG else 'Open Mic Night',
        'bugs': 'They\'re not bugs, they\'re improvised features! 🐛✨',
        'coffee_consumption': 'Dangerously high ☕',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo with attitude and commentary"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'error': 'No JSON data provided',
                'suggestion': 'Send me something! I promise to echo it back with style! ✨',
                'mood': 'Disappointed but hopeful'
            }), 400
        
        logger.info(f"Got some data to echo: {data}")
        
        commentary = [
            "Nice JSON! Your formatting skills are on point! 👌",
            "I see what you did there... classic! 😎",
            "Echoing this masterpiece back to you! 🎨",
            "Your data just made my day! Thanks! 😊",
            "Processing... Beep boop... Echo complete! 🤖"
        ]
        
        return jsonify({
            'received': data,
            'echo_commentary': random.choice(commentary),
            'echo_quality': f"{random.randint(9, 10)}/10 - Premium Echo Service! 📢",
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    except Exception as e:
        logger.error(f"Echo failed spectacularly: {str(e)}")
        return jsonify({
            'error': 'Echo machine broke! 💔',
            'technical_details': 'Something went hilariously wrong',
            'suggested_fix': 'Try turning it off and on again... or send better data! 😉'
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors with humor"""
    logger.warning(f"Someone got lost looking for: {request.path} 🗺️")
    
    funny_404s = [
        "This page is like my motivation on Monday morning... nowhere to be found! 😴",
        "Error 404: Humor not found... wait, that's ironic! 🤔",
        "This endpoint is hiding better than my bugs in production! 🙈",
        "You've discovered the Bermuda Triangle of APIs! 🌊",
        "This page is taking a vacation. Try again later! 🏖️"
    ]
    
    return jsonify({
        'error': '🚫 Oops! Page Not Found! 🚫',
        'funny_message': random.choice(funny_404s),
        'path': request.path,
        'suggestion': 'Try /, /joke, /dadjoke, /roast, /fact, /insult, /motivate, or /health',
        'status': 404,
        'lost_level': 'Extremely lost! 🧭'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors with humor"""
    logger.error(f"Everything is on fire! 🔥: {str(error)}")
    
    return jsonify({
        'error': '💥 Something Exploded! 💥',
        'technical_explanation': 'The hamsters running this server need a coffee break ☕',
        'status': 500,
        'panic_level': 'Maximum overdrive! 😱',
        'solution': 'Turn it off and on again... or sacrifice a rubber duck to the code gods! 🦆'
    }), 500


@app.before_request
def log_request():
    """Log incoming requests with style"""
    funny_prefixes = ["🎯", "🚀", "🎪", "🎭", "🎨", "⚡", "🔥", "✨"]
    prefix = random.choice(funny_prefixes)
    logger.info(f"{prefix} {request.method} {request.path} - Let the comedy begin!")


if __name__ == "__main__":
    logger.info(f"🎪 Starting the Comedy Flask Circus on {HOST}:{PORT} 🎪")
    logger.info("🎭 Prepare for maximum hilarity! 🎭")
    logger.info("☕ Coffee level: Critical ☕")
    logger.info("🐛 Bug status: They're features now! 🐛")
    app.run(host=HOST, port=PORT, debug=DEBUG)