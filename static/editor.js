document.addEventListener("DOMContentLoaded", function () {
    const editor = document.getElementById("note");
    const saveBtn = document.getElementById("save");

    saveBtn.addEventListener("click", function () {
        alert("Note saved: " + editor.value);
        // You can later replace this with an actual POST request
    });
});

