<?php


$val = $_POST['equation'];
$param = $_POST['param'];
$file = fopen("infix.txt", "w");
fwrite($file, $val);
fclose($file);
$file = fopen("param.txt", "w");
fwrite($file, $param);
fclose($file);
exec('toRPN.exe');
exec('RPN_calc.exe');

$file_res = fopen("res.txt", "r");

$res = fread($file_res, filesize('res.txt'));
echo($val);
echo("\n");
echo($res);

fclose($file_res);

$test = fopen("infix.txt", "r");
$infix = fread($test, filesize('infix.txt'));
fclose($test);

