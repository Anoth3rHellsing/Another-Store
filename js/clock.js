// Shared clock widget for Another Store subpages
// Displays local browser time in 12-hour format with AM/PM suffix.
(function () {
  function updateClock() {
    var el = document.getElementById('clock');
    if (!el) return;
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;
    var minStr = minutes < 10 ? '0' + minutes : '' + minutes;
    el.textContent = hours + ':' + minStr + ' ' + ampm;
  }
  updateClock();
  setInterval(updateClock, 1000);
})();