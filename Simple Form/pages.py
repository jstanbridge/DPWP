'''
James Stanbridge
13 Feb 2015
Design Patterns for Web programming
Simple Form
'''

class Page(object): #initialization of our Page class
    def __init__(self): #self declaration, work like "this" in JavaScript

        #creating the attribute self.head and making it accessible outside of the class
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
            <img src="images/smite_logo_sm.png"><!-- logo img for smite / copyright HI-REZ Studios, Inc. / noncommercial use -->
        </header>
        """

        #creating the attribute self.form and making it accessible outside of the class
        self.form = """
            <form method=GET><!-- GET method used to communicate with python -->
                <p class="first"><label>Smite username: </label><br /><input type="text" name="su_name" /></p><!-- input #1 / text / collect username -->
                <p><label>Favorite god: </label><br /><input type="text" name="fav_god" /></p><!-- input #2 / text / collect favorite god -->
                <p>What is your preferred role?<br /><!-- input #3 / radio / collect favorite role -->
                    <input type="radio" name="role" value="Assassin" id="Assassin" /><label class="radio" for="Assassin">Assassin</label>
                    <input type="radio" name="role" value="Guardian" id="Guardian" /><label class="radio" for="Guardian">Guardian</label>
                    <input type="radio" name="role" value="Hunter" id="Hunter" /><label class="radio" for="Hunter">Hunter</label>
                    <input type="radio" name="role" value="Mage" id="Mage" /><label class="radio" for="Mage">Mage</label>
                    <input type="radio" name="role" value="Warrior" id="Warrior" /><label class="radio" for="Warrior">Warrior</label></p>
                <p><label>What is your preferred game mode?</label><br /><!-- input #4 / select / collect favorite game mode -->
                    <select name="game_mode">
                        <option value="Assault">Assault</option>
                        <option value="Conquest">Conquest</option>
                        <option value="Joust">Joust</option>
                        <option value="Siege">Siege</option>
                        <option value="Arena">Arena</option>
                    </select></p>
                <p class="last"><label><input type="checkbox" name="tac"> I agree to abide by the Grievance Organizational Charter.</label></p>
                <!-- input #5 / checkbox / collect acceptance of terms and conditions -->
                <input type="submit" value="submit" /><!-- input #6 / submit / submit form information -->
            </form>
        """

        #creating the attribute self.results and making it accessible outside of the class
        self.results = """
        <!-- this section is included prior to the python printing of results and is appended before the results via the page_results variable -->
        <p class="thanks">Thanks for joining Grievance!<br /> We look forward to seeing you in-game!</p>
        <p class="info">You entered the following information:</p>
        """


        #creating the attribute self.close and making it accessible outside of the class
        self.close = """
            <footer>
            <p><a href="http://www.grievancegaming.org/">www.grievancegaming.org</a></p>
            </footer>
        </div>
     </body>
</html>
        """

