<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space Invaders - Web Version</title>
    <style>
        canvas {
            background-color: black;
            display: block;
            margin: 0 auto;
        }
        #startButton {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            font-size: 20px;
            background-color: green;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <button id="startButton">BAŞLAT</button>
    <canvas id="gameCanvas" width="640" height="480"></canvas>

    <script src="game.js"></script>
</body>
</html>
