const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let player = {
    x: canvas.width / 2 - 25,
    y: canvas.height - 50,
    width: 50,
    height: 50,
    speed: 5,
    color: 'blue'
};

let enemies = [];
let bullets = [];
let isGameRunning = false;

// Oyunu başlat butonu
document.getElementById('startButton').addEventListener('click', startGame);

// Oyunu başlatma fonksiyonu
function startGame() {
    isGameRunning = true;
    document.getElementById('startButton').style.display = 'none'; // Butonu gizle
    requestAnimationFrame(gameLoop);
}

// Oyuncuyu çizme
function drawPlayer() {
    ctx.fillStyle = player.color;
    ctx.beginPath();
    ctx.moveTo(player.x + player.width / 2, player.y);
    ctx.lineTo(player.x, player.y + player.height);
    ctx.lineTo(player.x + player.width, player.y + player.height);
    ctx.closePath();
    ctx.fill();
}

// Düşmanları çizme (basit bir örnek)
function drawEnemies() {
    for (let i = 0; i < enemies.length; i++) {
        let enemy = enemies[i];
        ctx.fillStyle = 'red';
        ctx.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
    }
}

// Mermi çizme
function drawBullets() {
    for (let i = 0; i < bullets.length; i++) {
        let bullet = bullets[i];
        ctx.fillStyle = 'yellow';
        ctx.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    }
}

// Oyun döngüsü
function gameLoop() {
    if (!isGameRunning) return;

    // Temizle
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Çizimler
    drawPlayer();
    drawEnemies();
    drawBullets();

    // Oyuncuyu hareket ettir
    updatePlayer();
    updateBullets();

    requestAnimationFrame(gameLoop);
}

// Klavye kontrolleri
document.addEventListener('keydown', function (event) {
    if (event.code === 'ArrowLeft' && player.x > 0) {
        player.x -= player.speed;
    } else if (event.code === 'ArrowRight' && player.x + player.width < canvas.width) {
        player.x += player.speed;
    } else if (event.code === 'Space') {
        fireBullet();
    }
});

// Oyuncunun hareketini güncelleme
function updatePlayer() {
    // Oyuncu güncelleme
}

// Mermiyi ateşleme
function fireBullet() {
    bullets.push({
        x: player.x + player.width / 2 - 5,
        y: player.y,
        width: 10,
        height: 20,
        speed: 5
    });
}

// Mermiyi güncelleme
function updateBullets() {
    for (let i = 0; i < bullets.length; i++) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < 0) {
            bullets.splice(i, 1); // Mermi sahneyi terk ederse sil
        }
    }
}

// Basit düşman oluşturma
function spawnEnemies() {
    enemies.push({
        x: Math.random() * (canvas.width - 30),
        y: 0,
        width: 30,
        height: 30,
        speed: 2
    });
}

// Düşmanları güncelleme
function updateEnemies() {
    for (let i = 0; i < enemies.length; i++) {
        enemies[i].y += enemies[i].speed;
        if (enemies[i].y > canvas.height) {
            enemies.splice(i, 1); // Düşman sahneyi terk ederse sil
        }
    }
}

// Her birkaç saniyede bir düşman üret
setInterval(spawnEnemies, 2000);

