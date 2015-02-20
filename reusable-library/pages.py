class ResultsPage(object):
    #this is our results page class that will be called if the user has input data into the form
    def __init__(self):
        #here we are declaring a default title and css link
        self.__title = "Welcome"
        self.css = "css/styles.css"
        #below is our attribute containing the head portion of our html
        self.__head = """

<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calculator</title>
		<link href="css/styles.css" rel="Stylesheet" type="text/css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Quicksand:400,700' rel='stylesheet' type='text/css'>
	</head>
    <body>

    	<div id="container">

		<header>
			<h1>Team Stats Calculator</h1>
		</header>
        """
        #next we have the attribute containing our body html, which is empty because it is formed using elements in our main.py file
        self.body = ""
        self.__error = ''
        #finally, we have our closing html content contained in the close attribute
        self.close = """
        	<footer>
				<p>Cool footer stuff.</p>
			</footer>
        </div>
    </body>
</html>
        """
    #the below function prints the combined content of our attributes and allows them to be written onto the page
    def print_out(self):
        all = self.__head + self.body + self.__error + self.close
        return all


#this is our form page class that will be called if the user has not input data into the form
class FormPage(object):
    def __init__(self):
        #here we are declaring a default title and css link
        self.__title = "Welcome"
        self.css = "css/styles.css"
        #below is our attribute containing the head portion of our html
        self.__head = """

<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calculator</title>
		<link href="css/styles.css" rel="Stylesheet" type="text/css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Quicksand:400,700' rel='stylesheet' type='text/css'>
	</head>
    <body>
        """
        #next we have the attribute containing our body html, which is comprised of the form used to gather user input
        self.body = """

		<div id="container">

			<header>
				<h1>Team Stats Calculator</h1>
			</header>

			<div id="inst">
				<p>Enter the following information for each player on your team in order to calculate some stuff.</p>
			</div>

			<form>
				<fieldset>
				<legend>Player #1</legend>
				<p><label>Player Name: <input type="text" name="p1_name" required></label></p>
				<p><label>Kills: <input type="number" name="p1_kills" required></label></p>
				<p><label>Deaths: <input type="number" name="p1_deaths" required></label></p>
				<p><label>Assists: <input type="number" name="p1_assists" required></label></p>
				<p><label>Healing Done: <input type="number" name="p1_heals" required></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p1_abs" required></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #2</legend>
				<p><label>Player Name: <input type="text" name="p2_name" required></label></p>
				<p><label>Kills: <input type="number" name="p2_kills" required></label></p>
				<p><label>Deaths: <input type="number" name="p2_deaths" required></label></p>
				<p><label>Assists: <input type="number" name="p2_assists" required></label></p>
				<p><label>Healing Done: <input type="number" name="p2_heals" required></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p2_abs" required></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #3</legend>
				<p><label>Player Name: <input type="text" name="p3_name" required></label></p>
				<p><label>Kills: <input type="number" name="p3_kills" required></label></p>
				<p><label>Deaths: <input type="number" name="p3_deaths" required></label></p>
				<p><label>Assists: <input type="number" name="p3_assists" required></label></p>
				<p><label>Healing Done: <input type="number" name="p3_heals" required></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p3_abs" required></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #4</legend>
				<p><label>Player Name: <input type="text" name="p4_name" required></label></p>
				<p><label>Kills: <input type="number" name="p4_kills" required></label></p>
				<p><label>Deaths: <input type="number" name="p4_deaths" required></label></p>
				<p><label>Assists: <input type="number" name="p4_assists" required></label></p>
				<p><label>Healing Done: <input type="number" name="p4_heals" required></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p4_abs" required></label></p>
				</fieldset>

				<fieldset id="last">
				<legend>Player #5</legend>
				<p><label>Player Name: <input type="text" name="p5_name" required></label></p>
				<p><label>Kills: <input type="number" name="p5_kills" required></label></p>
				<p><label>Deaths: <input type="number" name="p5_deaths" required></label></p>
				<p><label>Assists: <input type="number" name="p5_assists" required></label></p>
				<p><label>Healing Done: <input type="number" name="p5_heals" required></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p5_abs" required></label></p>
				</fieldset>

				<input type="submit" value="Submit">
			</form>
        """
        self.__error = ''
        #finally, we have our closing html content contained in the close attribute
        self.close = """
        	<footer>
				<p>Cool footer stuff.</p>
			</footer>

		</div>
    </body>
</html>
        """
    #the below function prints the combined content of our attributes and allows them to be written onto the page
    def print_out(self):
        all = self.__head + self.body + self.__error + self.close
        return all
