#code gemaakt door Jaiel
#code stijl + javascript en functies gegenereerd door ai

html = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Morsecode For Dummies</title>

<script>
window.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", () => {
            fetch(`/letter?char=${btn.textContent}`).catch(err => console.error(err));
        });
    });
});
</script>

<style>
:root{
    --bg:#09090f;
    --glass:rgba(255,255,255,.05);
    --border:rgba(255,255,255,.08);
    --accent:#ff3b5c;
}

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Inter,Segoe UI,sans-serif;
}

body{
    min-height:100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    gap:35px;
    background:
        radial-gradient(circle at top,#4a101a 0%,transparent 50%),
        radial-gradient(circle at bottom,#7a1125 0%,transparent 50%),
        var(--bg);
    overflow:hidden;
}

h1{
    font-size:3rem;
    font-weight:900;
    letter-spacing:-1px;
    text-align:center;
    background:linear-gradient(90deg,#ffffff,#ff5b7d);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(255,59,92,.3);
}

.keyboard{
    display:flex;
    flex-direction:column;
    gap:14px;
    padding:32px;
    border-radius:32px;
    background:var(--glass);
    backdrop-filter:blur(30px);
    border:1px solid var(--border);
    box-shadow:
        0 25px 80px rgba(0,0,0,.55),
        0 0 40px rgba(255,59,92,.12),
        inset 0 1px 0 rgba(255,255,255,.08);
}

.row{
    display:flex;
    justify-content:center;
    gap:14px;
}

button{
    width:74px;
    height:74px;
    border:none;
    border-radius:20px;
    background:linear-gradient(
        180deg,
        rgba(255,255,255,.14),
        rgba(255,255,255,.04)
    );
    color:white;
    font-size:1.25rem;
    font-weight:700;
    cursor:pointer;
    border:1px solid rgba(255,255,255,.08);
    transition:all .2s ease;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,.08),
        0 8px 20px rgba(0,0,0,.25);
}

button:hover{
    transform:translateY(-4px);
    border-color:rgba(255,91,125,.7);
    box-shadow:
        0 0 24px rgba(255,59,92,.6),
        0 10px 30px rgba(0,0,0,.35);
}

button:active{
    transform:translateY(2px) scale(.96);
    box-shadow:
        0 0 15px rgba(255,59,92,.4);
}
</style>
</head>
<body>

<h1>Morscode For Dummies</h1>

<section class="keyboard">

    <div class="row">
        <button>Q</button>
        <button>W</button>
        <button>E</button>
        <button>R</button>
        <button>T</button>
        <button>Y</button>
        <button>U</button>
        <button>I</button>
        <button>O</button>
        <button>P</button>
    </div>

    <div class="row">
        <button>A</button>
        <button>S</button>
        <button>D</button>
        <button>F</button>
        <button>G</button>
        <button>H</button>
        <button>J</button>
        <button>K</button>
        <button>L</button>
    </div>

    <div class="row">
        <button>Z</button>
        <button>X</button>
        <button>C</button>
        <button>V</button>
        <button>B</button>
        <button>N</button>
        <button>M</button>
    </div>

</section>

</body>
</html>
"""
