const optionMenu = document.querySelector(".weather-menu"),
      WeatherSelectBtn = optionMenu.querySelector(".weather-btn"),
      options = optionMenu.querySelectorAll(".option"),
      wBtn_text = optionMenu.querySelector(".wBtn-text");

WeatherSelectBtn.addEventListener("click", () => optionMenu.classList.toggle("active"));

options.forEach(option => {
    option.addEventListener("click", () => {
        let selectedOption = option.querySelector(".option-text").innerText;
        wBtn_text.innerText = selectedOption;
        
        optionMenu.classList.toggle("active");
    });
});

const shadeMenu = document.querySelector(".shade-menu"),
      ShadeSelectionBtn = shadeMenu.querySelector(".shade-btn"),
      shadeOptions = shadeMenu.querySelectorAll(".shade-option"),
      sBtn_text = shadeMenu.querySelector(".sBtn-text");

ShadeSelectionBtn.addEventListener("click", () => shadeMenu.classList.toggle("active"));

shadeOptions.forEach(option => {
    option.addEventListener("click", () => {
        let selectedShadeOption = option.querySelector(".sOption-text").innerText;
        sBtn_text.innerText = selectedShadeOption;

        shadeMenu.classList.toggle("active");
    });
});

document.getElementById("selectionForm").addEventListener("submit", (event) => {
    event.preventDefault();
    const encodedWeather = encodeURIComponent(document.querySelector(".wBtn-text").innerText); // URL-encode the weather value
    const encodedShade = encodeURIComponent(document.querySelector(".sBtn-text").innerText); // URL-encode the shade value
    const url = `/generator/${encodedWeather}/${encodedShade}`;
    window
        .fetch(url)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("generated").innerHTML = data.generated;
        });
});