<?php

$filename = "domains.txt";

$myfile = fopen($filename, "r") or die("Unable to open file!");

// Add each line to an array
$arrayDomains = file($filename, FILE_IGNORE_NEW_LINES);

$results = array();

foreach ($arrayDomains as $key => $value) {
  $ip = gethostbyname($value);

  array_push($results, array("url" => $value, "ip" => $ip));
}

echo json_encode($results);

?>
