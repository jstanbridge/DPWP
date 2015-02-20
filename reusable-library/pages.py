class ResultsPage(object):
    def __init__(self):
        self.__title = "Welcome"
        self.css = "css/styles.css"
        self.__head = """

<!DOCTYPE HTML>
<html>
    <head>
        <title>Team Stats Calculator</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
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
        <title>Team Stats Calculator</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = """

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Team Stats Calulator</title>
	</head>
	<body>

		<div id="container">

			<header>
				<p>Cool header stuff.</p>
			</header>

			<div id="inst">
				<p>Enter the following information for each player on your team in order to calculate some stuff.</p>
			</div>

			<form>
				<h2>Player #1</h2>
				<p><label>Player Name: </label><input type="text" name="p1_name"></p>
				<p><label>Kills: </label><input type="text" name="p1_kills"></p>
				<p><label>Deaths: </label><input type="text" name="p1_deaths"></p>
				<p><label>Assists: </label><input type="text" name="p1_assissts"></p>
				<p><label>Healing Done: </label><input type="text" name="p1_heals"></p>
				<p><label>Damage Mitigated: </label><input type="text" name="p1_abs"></p>
			</form>

			<form>
				<h2>Player #2</h2>
				<p><label>Player Name: </label><input type="text" name="p2_name"></p>
				<p><label>Kills: </label><input type="text" name="p2_kills"></p>
				<p><label>Deaths: </label><input type="text" name="p2_deaths"></p>
				<p><label>Assists: </label><input type="text" name="p2_assissts"></p>
				<p><label>Healing Done: </label><input type="text" name="p2_heals"></p>
				<p><label>Damage Mitigated: </label><input type="text" name="p2_abs"></p>
			</form>

			<form>
				<h2>Player #3</h2>
				<p><label>Player Name: </label><input type="text" name="p3_name"></p>
				<p><label>Kills: </label><input type="text" name="p3_kills"></p>
				<p><label>Deaths: </label><input type="text" name="p3_deaths"></p>
				<p><label>Assists: </label><input type="text" name="p3_assissts"></p>
				<p><label>Healing Done: </label><input type="text" name="p3_heals"></p>
				<p><label>Damage Mitigated: </label><input type="text" name="p3_abs"></p>
			</form>

			<form>
				<h2>Player #4</h2>
				<p><label>Player Name: </label><input type="text" name="p4_name"></p>
				<p><label>Kills: </label><input type="text" name="p4_kills"></p>
				<p><label>Deaths: </label><input type="text" name="p4_deaths"></p>
				<p><label>Assists: </label><input type="text" name="p4_assissts"></p>
				<p><label>Healing Done: </label><input type="text" name="p4_heals"></p>
				<p><label>Damage Mitigated: </label><input type="text" name="p4_abs"></p>
			</form>

			<form>
				<h2>Player #5</h2>
				<p><label>Player Name: </label><input type="text" name="p5_name"></p>
				<p><label>Kills: </label><input type="text" name="p5_kills"></p>
				<p><label>Deaths: </label><input type="text" name="p5_deaths"></p>
				<p><label>Assists: </label><input type="text" name="p5_assissts"></p>
				<p><label>Healing Done: </label><input type="text" name="p5_heals"></p>
				<p><label>Damage Mitigated: </label><input type="text" name="p5_abs"></p>
			</form>

			<footer>
				<p>Cool footer stuff.</p>
			</footer>

		</div>

	</body>
</html>




        """
        self.__error = ''
        self.close = """
    </body>
</html>
        """
    def print_out(self):
        all = self.__head + self.body + self.__error + self.close
        return all
