function signIn() {
  gapi.load('client:auth2', initClient);
};

function initClient() {
  gapi.client.init({
    clientId: '114457300838-o2ekjbfotm4qb9qaaenfue6ohvptpbs1.apps.googleusercontent.com',
    scope: 'https://www.googleapis.com/auth/calendar'
  }).then(function () {
    gapi.auth2.getAuthInstance().signIn();
  });
};


    function handleSignedIn(googleUser) {
      var events = [];
      var eventList = document.getElementById('eventList');
      gapi.client.load('calendar', 'v3', function () {
        var request = gapi.client.calendar.events.list({
          'calendarId': 'primary',
          'timeMin': (new Date()).toISOString(),
          'showDeleted': false,
          'singleEvents': true,
          'maxResults': 10,
          'orderBy': 'startTime'
        });
    
        request.execute(function (resp) {
          { for

client_id = gapi.auth2.init();

function onSignIn(googleUser) {
    let profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
  };


  //Attempt to redirect to homepage using Calendar button on Edit Patient page. 
  document.addEventListener('DOMContentLoaded', function() {
    // Get the button element
    let calendarButton = document.getElementById('calendar-btn');

    // Add a click event listener to the button
    calendarButton.addEventListener('click', function() {
        // Redirect to another page within the same app
        window.location.href = "/calendar";
    });
  });