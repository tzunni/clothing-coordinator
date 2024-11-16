const optionMenu = document.querySelector(".weather-menu"),
    WeatherSelectBtn = optionMenu.querySelector(".weather-btn"),
    options = optionMenu.querySelectorAll(".option"),
    wBtn_text = optionMenu.querySelector(".wBtn-text");

WeatherSelectBtn.addEventListener("click", () => optionMenu.classList.toggle("active"));

options.forEach(option =>{
    option.addEventListener("click", () =>{
        let selectedOption = option.querySelector(".option-text").innerText;
        wBtn_text.innerText = selectedOption;
        
        optionMenu.classList.toggle("active");
    });
});