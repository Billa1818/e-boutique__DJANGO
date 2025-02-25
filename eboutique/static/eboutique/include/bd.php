<?php

$db_host="localhost";
$db_user="root";
$db_password="";
$db_name="e-boutique";

$conn =new mysqli($db_host,$db_user,$db_password,$db_name);

if($conn->connect_error){

  die("nous n'avont pas pu accerder a la base de données ".$conn->connect_error);
}
?>