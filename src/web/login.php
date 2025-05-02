<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    $params = [];
    parse_str($_SERVER['QUERY_STRING'], $params);
    
    if ($username === 'admin' && $password === 'bl4ckbl4ckbl4ck') {
        $_SESSION['username'] = $username;
        $_SESSION['role'] = $params['role'] ?? 'user';
        header('Location: index.php');
        exit;
    }
    
    $error = "Invalid credentials";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Secret Corp</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <?php if(isset($error)): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        
        <form method="POST">
            <div class="form-group">
                <label>Username:</label>
                <input type="text" name="username" required>
            </div>
            <div class="form-group">
                <label>Password:</label>
                <input type="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
