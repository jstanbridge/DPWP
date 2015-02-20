class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """

<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calulator</title>
		<link href="css/styles.css" rel="Stylesheet" type="text/css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Quicksand:400,700' rel='stylesheet' type='text/css'>
	</head>
    <body>
        """

        self.body = ""
        self.__error = ''
        self.close = """
    </body>
</html>
        """
    def print_out(self):
        all = self.__head + self.body + self.__error + self.close
        return all



class FormPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """

<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calulator</title>
		<link href="css/styles.css" rel="Stylesheet" type="text/css">
		<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Quicksand:400,700' rel='stylesheet' type='text/css'>
	</head>
    <body>
        """

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
				<p><label>Player Name: <input type="text" name="p1_name"></label></p>
				<p><label>Kills: <input type="number" name="p1_kills"></label></p>
				<p><label>Deaths: <input type="number" name="p1_deaths"></label></p>
				<p><label>Assists: <input type="number" name="p1_assists"></label></p>
				<p><label>Healing Done: <input type="number" name="p1_heals"></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p1_abs"></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #2</legend>
				<p><label>Player Name: <input type="text" name="p2_name"></label></p>
				<p><label>Kills: <input type="number" name="p2_kills"></label></p>
				<p><label>Deaths: <input type="number" name="p2_deaths"></label></p>
				<p><label>Assists: <input type="number" name="p2_assists"></label></p>
				<p><label>Healing Done: <input type="number" name="p2_heals"></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p2_abs"></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #3</legend>
				<p><label>Player Name: <input type="text" name="p3_name"></label></p>
				<p><label>Kills: <input type="number" name="p3_kills"></label></p>
				<p><label>Deaths: <input type="number" name="p3_deaths"></label></p>
				<p><label>Assists: <input type="number" name="p3_assists"></label></p>
				<p><label>Healing Done: <input type="number" name="p3_heals"></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p3_abs"></label></p>
				</fieldset>

				<fieldset>
				<legend>Player #4</legend>
				<p><label>Player Name: <input type="text" name="p4_name"></label></p>
				<p><label>Kills: <input type="number" name="p4_kills"></label></p>
				<p><label>Deaths: <input type="number" name="p4_deaths"></label></p>
				<p><label>Assists: <input type="number" name="p4_assists"></label></p>
				<p><label>Healing Done: <input type="number" name="p4_heals"></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p4_abs"></label></p>
				</fieldset>

				<fieldset id="last">
				<legend>Player #5</legend>
				<p><label>Player Name: <input type="text" name="p5_name"></label></p>
				<p><label>Kills: <input type="number" name="p5_kills"></label></p>
				<p><label>Deaths: <input type="number" name="p5_deaths"></label></p>
				<p><label>Assists: <input type="number" name="p5_assists"></label></p>
				<p><label>Healing Done: <input type="number" name="p5_heals"></label></p>
				<p><label>Damage Mitigated: <input type="number" name="p5_abs"></label></p>
				</fieldset>

				<input type="submit" value="Submit">
			</form>

			<footer>
				<p>Cool footer stuff.</p>
			</footer>

		</div>




        """
        self.__error = ''
        self.close = """
    </body>
</html>
        """
    def print_out(self):
        all = self.__head + self.body + self.__error + self.close
        return all
