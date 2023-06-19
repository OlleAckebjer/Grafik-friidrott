window.onload=start_time

function start_time () {
    var startTime = new Date().getTime();

    function updateTimer() {
        var currentTime = new Date().getTime();
        var elapsedTime = currentTime - startTime;

        var hours = Math.floor(elapsedTime / 3600000);
        var minutes = Math.floor((elapsedTime % 3600000) / 60000);
        var seconds = Math.floor((elapsedTime % 60000) / 1000);
        var milliseconds = elapsedTime % 100;

        // Add leading zeros to the values
        hours = padNumber(hours, 2);
        minutes = padNumber(minutes, 2);
        seconds = padNumber(seconds, 2);
        milliseconds = padNumber(milliseconds, 2);

        var timerElement = document.getElementById("timer");
        timerElement.textContent = hours + ":" + minutes + ":" + seconds + "." + milliseconds;

        // Update the timer every 10 milliseconds
        setTimeout(updateTimer, 10);
    }

    // Helper function to add leading zeros
    function padNumber(num, length) {
        return ("0" + num).slice(-length);
    }

    // Start the timer
    updateTimer();
};
