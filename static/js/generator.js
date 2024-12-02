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

const accessoryMenu = document.querySelector(".accessory-menu"),
      AccessorySelectBtn = accessoryMenu.querySelector(".accessory-btn"),
      accessoryOptions = accessoryMenu.querySelectorAll(".accessory-option"),
      aBtn_text = accessoryMenu.querySelector(".aBtn-text");

AccessorySelectBtn.addEventListener("click", () => accessoryMenu.classList.toggle("active"));

accessoryOptions.forEach(option => {
    option.addEventListener("click", () => {
        let selectedAccessoryOption = option.querySelector(".aOption-text").innerText;
        aBtn_text.innerText = selectedAccessoryOption;

        accessoryMenu.classList.toggle("active");
    });
});

document.getElementById("selectionForm").addEventListener("submit", (event) => {
    event.preventDefault();
    const encodedWeather = encodeURIComponent(document.querySelector(".wBtn-text").innerText);
    const encodedShade = encodeURIComponent(document.querySelector(".sBtn-text").innerText);
    const encodedAccessory = encodeURIComponent(document.querySelector(".aBtn-text").innerText);
    const url = `/generator/${encodedWeather}/${encodedShade}/${encodedAccessory}`;
    window
        .fetch(url)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("generated").innerHTML = data.generated;
        });
});
