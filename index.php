
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Math Solver</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
<body>
    <?php include ("nav.php"); ?>
    <div class="container col-15">

        <div class="menu col-3">
            <h1>Задачи</h1>
            <div class = "sidebar">
              <ul>
                <li>
                  <a href="index.php">Интегралы</a>
               </li>
                <li>
                  <a href="matrix.php">Матрицы</a>
                </li>
              </ul>
          </div>
        </div>

        <div class="calc col-8">
          <img src="icons8-integral-50.png" alt="integral">
          <div class="col">
              <input type="text" class="equation" value="x^2+x">
              <button name="letsgo" type="submit" class="btn btn-primary">Решить</button>
              <span>dx</span>
          </div>
          <div class="param col-1">
                <p>x<sub>1</sub>: </p><input type="text" class="a col-2" value="1">
                <p>x<sub>2</sub>: </p><input type="text" class="b col-2" value="10">
                <p>Разбиения: </p><input type="text" class="n col-2" value="100">
              </div>
          <div class="result" hidden>
            <p class="row" id="infix"></p>
            <p class="det row" id="det" hidden></p>
            <p class="step row" id="step" hidden></p>
            <p class="res row" id="res" hidden></p>
        </div>
        </div>

        <div class="info col-4">
          <h1>Инструкция</h1>
          <p>Возведение в степень задается сиволом - <span>^</span></p>
          <p>Если ты хочешь посчитать натуральный логарифм - пиши <span>log()</span></p>
          <p>А возведение экспоненты в степень делается так - <span>exp()</span></p>
        </div>

    </div>
    <script src="script.js"></script>
    <script type="text/javascript">
       $('.btn-primary').click(function (){
        const equationElement = document.querySelector(".equation");
        const equationValue = equationElement.value;
        const aElement = document.querySelector(".a");
        const aValue = aElement.value;
        const bElement = document.querySelector(".b");
        const bValue = bElement.value;
        const nElement = document.querySelector(".n");
        const nValue = nElement.value;
        var data = {
            equation: equationValue,
            param: aValue + " " + bValue + " " + nValue,
        };
        console.log(data);
        $.ajax({
            url: 'control.php',
            method: 'post',
            data: data,
            success:function(response){
              const arr = response.split("\n");
              const infix = arr[0];
              const det = arr[1];
              const step = arr[2];
              const res = arr[3];
              if (res == undefined)
              {
                document.getElementById("infix").innerHTML = 'Ошибка! Неверно введено подынтегральное выражение';
                const str1 = document.querySelector('.det');
                str1.setAttribute('hidden', 'true');
                const str2 = document.querySelector('.step');
                str2.setAttribute('hidden', 'true');
                const str3 = document.querySelector('.res');
                str3.setAttribute('hidden', 'true');
              }
              else
              {
                const str1 = document.querySelector('.det');
                str1.removeAttribute('hidden');
                const str2 = document.querySelector('.step');
                str2.removeAttribute('hidden');
                const str3 = document.querySelector('.res');
                str3.removeAttribute('hidden');
                document.getElementById("infix").innerHTML = 'Уравнение: ' + infix;
                document.getElementById("det").innerHTML = 'Разбиений: ' + det;
                document.getElementById("step").innerHTML = 'Шаг: ' + step;
                document.getElementById("res").innerHTML = 'Результат: ' + res;
              }
              const result = document.querySelector('.result');
              result.removeAttribute('hidden');
            }
        });
    })
    </script>
</body>
</html>