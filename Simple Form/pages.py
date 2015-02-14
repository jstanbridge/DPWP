'''
James Stanbridge
13 Feb 2015
Design Patterns for Web programming
Simple Form
'''

class Page(object):
    def __init__(self):

        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Apply to Join Grievance in Smite</title>
        <link href="css/styles.css" rel="Stylesheet" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Nothing+You+Could+Do' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu' rel='stylesheet' type='text/css'>
    </head>
    <body>

        <div id="container">
        <header>
            <h1>Join Grievance in:</h1>
            <img src="images/smite_logo_sm.png">
        </header>
        """

        self.form = """
            <form method=GET>
                <p class="first"><label>Smite username: </label><br /><input type="text" name="su_name" /></p>
                <p><label>Favorite god: </label><br /><input type="text" name="fav_god" /></p>
                <p>What is your preferred role?<br />
                    <input type="radio" name="role" value="Assassin" id="Assassin" /><label class="radio" for="Assassin">Assassin</label>
                    <input type="radio" name="role" value="Guardian" id="Guardian" /><label class="radio" for="Guardian">Guardian</label>
                    <input type="radio" name="role" value="Hunter" id="Hunter" /><label class="radio" for="Hunter">Hunter</label>
                    <input type="radio" name="role" value="Mage" id="Mage" /><label class="radio" for="Mage">Mage</label>
                    <input type="radio" name="role" value="Warrior" id="Warrior" /><label class="radio" for="Warrior">Warrior</label></p>
                <p><label>What is your preferred game mode?</label><br />
                    <select name="game_mode">
                        <option value="Assault">Assault</option>
                        <option value="Conquest">Conquest</option>
                        <option value="Joust">Joust</option>
                        <option value="Siege">Siege</option>
                        <option value="Arena">Arena</option>
                    </select></p>
                <p class="last"><label><input type="checkbox" name="tac"> I agree to abide by the Grievance Organizational Charter.</label></p>
                <input type="submit" value="submit" />
            </form>
        """

        self.results = """
        <p class="thanks">Thanks for joining Grievance!<br /> We look forward to seeing you in-game!</p>
        <p class="info">You entered the following information:</p>
        """

        self.close = """
            <footer>
            <p><a href="http://www.grievancegaming.org/">www.grievancegaming.org</a></p>
            </footer>
        </div>
     </body>
</html>
        """

