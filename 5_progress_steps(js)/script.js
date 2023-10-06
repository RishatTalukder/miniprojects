// Selecting the progress bar, previous and next buttons, and all the circles
const progress = document.getElementById("progress");
const prev = document.getElementById("prev");
const next = document.getElementById("next");
const circles = document.querySelectorAll(".circle");

// Setting the initial active step to 1
let currentActive = 1;

// Adding event listeners to the next and prev buttons
next.addEventListener("click", () => {
  // Incrementing the active step and ensuring it does not exceed the number of circles
  currentActive++;
  if (currentActive > circles.length) {
    currentActive = circles.length;
  }
  // Updating the progress bar and circles
  update();
});

prev.addEventListener("click", () => {
  // Decrementing the active step and ensuring it does not go below 1
  currentActive--;
  if (currentActive < 1) {
    currentActive = 1;
  }
  // Updating the progress bar and circles
  update();
});

/**
 * Updates the progress bar and circles based on the current active step
 */
function update() {
  // Updating the circles based on the current active step
  circles.forEach((circle, idx) => {
    if (idx < currentActive) {
      circle.classList.add("active");
    } else {
      circle.classList.remove("active");
    }
  });
  // Updating the width of the progress bar based on the number of active circles
  const actives = document.querySelectorAll(".active");
  progress.style.width =
    ((actives.length - 1) / (circles.length - 1)) * 100 + "%";
  // Disabling the prev button if the active step is 1, and disabling the next button if the active step is the last circle
  if (currentActive === 1) {
    prev.disabled = true;
  } else if (currentActive === circles.length) {
    next.disabled = true;
  } else {
    prev.disabled = false;
    next.disabled = false;
  }
}