<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="description" content="A Webpage created to be the home page of Undergraduate Research Projects" />
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

<!-- TABLE TO DISPLAY INFORMATION -->
<table>
<tr>
        <h2><br> Record of Attacks </h2>
</tr>

<th> Incident Number: </th>
<th> IP Address: </th>
<th> Time of Attack: </th>
<th> Status: </th>
<th> Message: </th>

<?php
$handle = fopen("/var/networkscout/stuff/webinfo", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        $attacks = explode(',', $line);
        ?>

		<tr>
        	<td> <?php echo $attacks[0]; ?> </td>
			<td> <?php echo $attacks[1]; ?> </td>
			<td> <?php echo $attacks[2]; ?> </td>
			<td> <?php echo $attacks[3]; ?> </td>
			<td> <?php echo $attacks[4]; ?> </td>
		<tr>

<?php }    

    fclose($handle);
  }
  else {
    echo "<script>alert('There was an error opening the log file. 001')</script>";
} 


 ?>

</table>


        <!-- SPACE DIV -->
        <div id="space"></div>


        </div>

        <!-- FOOTER OF THE WEBPAGE (ERROR DATE DOES NOT SHOW UP AT THE BOTTOM -->
        <div id="foot">
                <p>
<!-- PHP FUNCTION TO GET THE DATE -->
<?php
	
date_default_timezone_set('America/Indiana/Knox');
$date =  date("M, d Y");

echo "$date";

?>


                </p>

        </div>
</div>


</body>
</html>
