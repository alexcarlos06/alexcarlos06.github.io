const currentYearElement =
    document.querySelector("#current-year");

const currentYear =
    new Date().getFullYear();

if (currentYearElement) {
    currentYearElement.textContent =
        currentYear;
}