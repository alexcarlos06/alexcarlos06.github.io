const THEME_STORAGE_KEY = "alex-sousa-theme";
const rootElement = document.documentElement;

const icons = {
    dark: `
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20.4 15.5A8.2 8.2 0 0 1 8.5 3.6 8.6 8.6 0 1 0 20.4 15.5Z"></path>
        </svg>
    `,
    light: `
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
            <circle cx="12" cy="12" r="3.6"></circle>
            <path d="M12 2.5V5M12 19v2.5M4.6 4.6l1.8 1.8M17.6 17.6l1.8 1.8M2.5 12H5M19 12h2.5M4.6 19.4l1.8-1.8M17.6 6.4l1.8-1.8"></path>
        </svg>
    `,
};

function getSavedTheme() {
    try {
        return localStorage.getItem(THEME_STORAGE_KEY);
    } catch {
        return null;
    }
}

function saveTheme(theme) {
    try {
        localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch {
        // O tema continua funcionando mesmo quando o armazenamento está indisponível.
    }
}

function getCurrentTheme() {
    return rootElement.dataset.theme === "light" ? "light" : "dark";
}

function updateThemeButton(button, theme) {
    const isLight = theme === "light";
    button.innerHTML = icons[theme];
    button.setAttribute(
        "aria-label",
        isLight ? "Ativar modo escuro" : "Ativar modo claro"
    );
    button.setAttribute(
        "title",
        isLight ? "Ativar modo escuro" : "Ativar modo claro"
    );
    button.setAttribute("aria-pressed", String(isLight));
}

function applyTheme(theme, button) {
    rootElement.dataset.theme = theme;
    rootElement.style.colorScheme = theme;

    if (button) {
        updateThemeButton(button, theme);
    }
}

function createThemeToggle() {
    const navContent = document.querySelector(".nav-content");

    if (!navContent) {
        return null;
    }

    const button = document.createElement("button");
    button.type = "button";
    button.className = "btn btn-icon theme-toggle";
    button.dataset.themeToggle = "";

    navContent.appendChild(button);

    button.addEventListener("click", () => {
        const nextTheme = getCurrentTheme() === "dark" ? "light" : "dark";
        applyTheme(nextTheme, button);
        saveTheme(nextTheme);
    });

    return button;
}

const themeToggle = createThemeToggle();
const savedTheme = getSavedTheme();
applyTheme(savedTheme === "light" ? "light" : "dark", themeToggle);

const currentYearElement =
    document.querySelector("#current-year");

const currentYear =
    new Date().getFullYear();

if (currentYearElement) {
    currentYearElement.textContent =
        currentYear;
}
