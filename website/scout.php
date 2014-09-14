<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="description" content="A Webpage created to be the home page of Undergraduate Research Proje$
<meta name="keywords" content="Network-Scout, Security, Undergraduate Research" />
<meta name="author" content="Aedan Somerville and Shawn Jordan" />
<meta HTTP-EQUIV="refresh" content="100">

<title>Scout-Server</title>

<link rel="stylesheet" type="text/css" href="scoutserver.css" />

</head>

<body>

<!-- HEADER OF THE WEB PAGE -->
<div id="head">
        <h1>
        <strong>Scout-Network</strong>
        </h1>
</div>


<!-- MAIN CONTENT AREA OF THE WEBPAGE -->
<div id="main">

        <div id="output_div">
<?php

//ASSIGN VARIABLES
$host = "localhost";
$usr = "root";
$pwd = "raspberry";
$db = "Network_Scout";

//CONNECT TO MYSQL DATABASE AND EXTRACT DATA FROM TABLE
$link = mysql_connect($host, $usr, $pwd) or die(mysql_error());
mysql_select_db($db) or die(mysql_error());
$query = "SELECT * FROM Attacks";
$result = mysql_query($query);

?>

<!-- TABLE TO DISPLAY INFORMATION -->
<table>
<tr>
        <h2><br> Record of Attacks </h2>
</tr>

<th> Incident Number: </th>
<th> Ip Address: </th>
<th> Time of Attack: </th>
<th> Status: </th>
<th> Message: </th>

<?php
while ($line = mysql_fetch_array($result))
{ ?>

<tr>
        <td> <? echo $line["incident_number"]; ?> </td>
        <td> <? echo $line["rpi_ip"]; ?> </td>
        <td> <? echo $line["time"]; ?> </td>
        <td> <? echo $line["alert_level"]; ?> </td>
        <td> <? echo $line["message"]; ?>
<tr>

<?php } ?>

</table>

<?php
//CLOSE THE MYSQL CONNECTION
mysql_close($link);
?>

        <!-- SPACE DIV -->
        <div id="space"></div>


        </div>

        <!-- FOOTER OF THE WEBPAGE (ERROR DATE DOES NOT SHOW UP AT THE BOTTOM -->
        <div id="foot">
                <p>
<!-- PHP FUNCTION TO GET THE DATE -->
<?php

$date =  date("M, d Y");

echo "$date";

?>


                </p>

        </div>
</div>


</body>
</html>