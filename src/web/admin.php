<?php
session_start();

if (!isset($_SESSION['role']) || $_SESSION['role'] !== 'admin') {
    session_destroy();
    header('Location: index.php');
    exit;
}

$flag = "CODEBY{REDACTED}";
?>

<!DOCTYPE html>
<html>
<head>
    <title>Secret Corp</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h2>Admin Panel</h2>
        <div class="flag-container">
            <p>Congratulations! Here's your flag:</p>
            <div class="flag"><?php echo $flag; ?></div>
        </div>
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>
