$(document).ready(function () {

    var premierClubs = ['Arsenal', 'A.F.C. Bournemouth', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield Town', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Southampton', 'Stoke City', 'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United'];
    var bundesClubs = ['1. FC Köln', '1899 Hoffenheim', 'Bayer Leverkusen', 'Bayern Munich', 'Borussia Dortmund', 'Borussia Mönchengladbach', 'Eintracht Frankfurt', 'FC Augsburg', 'Hamburger SV', 'Hannover 96', 'Hertha BSC', 'Mainz 05', 'RB Leipzig', 'SC Freiburg', 'Schalke 04', 'VfB Stuttgart', 'VfL Wolfsburg', 'Werder Bremen'];
    var eredivisieClubs = ['ADO Den Haag', 'Ajax', 'AZ', 'Excelsior', 'Feyenoord', 'Groningen', 'Heerenveen', 'Heracles Almelo', 'NAC Breda', 'PEC Zwolle', 'PSV', 'Roda JC', 'Sparta Rotterdam', 'Twente', 'Utrecht', 'Vitesse', 'VVV-Venlo', 'Willem II'];
    var laLigaClubs = ['Alavés', 'Athletic Bilbao', 'Atlético Madrid', 'Barcelona', 'Celta Vigo', 'Deportivo La Coruña', 'Eibar', 'Espanyol', 'Getafe', 'Girona', 'Las Palmas', 'Leganés', 'Levante', 'Málaga', 'Real Betis', 'Real Madrid', 'Real Sociedad', 'Sevilla', 'Valencia', 'Villarreal'];
    var ligue1Clubs = ['AS Monaco', 'Angers', 'Bordeaux', 'Caen', 'Dijon FCO', 'Guingamp', 'Lille', 'Lyon', 'Marseille', 'Metz', 'Montpellier', 'Nantes', 'Nice', 'Paris Saint-Germain', 'SC Amiens', 'Saint-Etienne', 'Stade Rennes', 'Strasbourg', 'Toulouse', 'Troyes'];
    var serieAClubs = ['Atalanta', 'Benevento', 'Bologna', 'Cagliari', 'Chievo', 'Crotone', 'Fiorentina', 'Genoa', 'Hellas Verona', 'Internazionale', 'Juventus', 'Lazio', 'Milan', 'Napoli', 'Roma', 'Sampdoria', 'Sassuolo', 'SPAL', 'Torino', 'Udinese'];
    var leagues = [premierClubs, bundesClubs, eredivisieClubs, laLigaClubs, ligue1Clubs, serieAClubs];
    var num = Math.floor(Math.random() * leagues.length);
    var league = leagues[num];
    var num = Math.floor(Math.random() * league.length);
    $(".result").text(league[num]);

})