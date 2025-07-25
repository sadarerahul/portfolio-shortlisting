document.addEventListener("DOMContentLoaded", function () {
    const themeSwitcher = document.getElementById("themeSwitcher");
    if (!themeSwitcher) return;

    // Check saved mode
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
        themeSwitcher.checked = true;
    }

    themeSwitcher.addEventListener("change", () => {
        if (themeSwitcher.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("theme", "dark");
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("theme", "light");
        }
    });
});
