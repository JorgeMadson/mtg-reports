from flask import Flask, render_template, request, redirect, url_for
from simplao_model import db, Event, Location, Player, Deck, Report

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    reports = Report.query.all()
    return render_template('index.html', reports=reports)

@app.route('/add_report', methods=['GET', 'POST'])
def add_report():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        location_name = request.form['location_name']
        player_name = request.form['player_name']
        deck_name = request.form['deck_name']
        matches_played = request.form['matches_played']
        matches_won = request.form['matches_won']
        final_ranking = request.form['final_ranking']

        event = Event(name=event_name, date=event_date, location=location_name, players_count=0)
        location = Location(name=location_name)
        player = Player(name=player_name)
        deck = Deck(name=deck_name)

        db.session.add(event)
        db.session.add(location)
        db.session.add(player)
        db.session.add(deck)
        db.session.commit()

        report = Report(matches_played=matches_played, matches_won=matches_won, final_ranking=final_ranking,
                        event_id=event.id, player_id=player.id, deck_id=deck.id)
        db.session.add(report)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_report.html')

@app.route('/insights')
def insights():
    # Aqui você pode adicionar lógica para gerar insights
    return render_template('insights.html')
