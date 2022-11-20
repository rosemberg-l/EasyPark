<?php
    $user = "root";
    $pass = "";
    $server = "localhost";
    $db = "easypark";
    $conn = mysqli_connect($server,$user,$pass,$db); 
    
    if(!$conn){
        echo 'Fallo de la conexión';
    }else{
        echo 'Conexión exitosa';} 

    return $conn;
?>

