from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
from hangman import Hangman, Fruit_word_list, hangman_drawing
wumpus_game = HuntTheWumpus()
hangman_game = Hangman(Fruit_word_list(), hangman_drawing())
hangman_game.display_man()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wumpus', methods=['POST', 'GET'])
def wumpus():
    if request.method == 'POST':
        message = wumpus_game.play(request.form)
    else:
        message = wumpus_game.new_game()
    return render_template('wumpus.html', message=message, game=wumpus_game)
@app.route('/Hangman', methods=['GET', 'POST'] )
def hangman():
    return render_template('HangMan.html', welcome_message = hangman_game.welcome_message, display_man = hangman_game.display_man)

if __name__ == "__main__":
    app.run()