document.getElementById("family-profile-photo").addEventListener("click", function() {
    document.getElementById("family-profile-input").click();
});

document.getElementById("family-profile-input").addEventListener("change", function(e) {
    var file = e.target.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
        document.getElementById("selected-profile-img").src = event.target.result;
    };

    reader.readAsDataURL(file);
});

document.getElementById("family-cover-photo").addEventListener("click", function() {

    document.getElementById("family-cover-input").click();
});

document.getElementById("family-cover-input").addEventListener("change", function(e) {
    var file = e.target.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
        document.getElementById("selected-cover-img").src = event.target.result;
    };

    reader.readAsDataURL(file);
});



const driver = window.driver.js.driver;

const driverObj = driver({
    showProgress: true,
    allowClose: false,
    steps: [
      { element: '#family-name', popover: { title: 'Choose a Name', description: 'Names are not unique but family ID is! We will have family ID in your family profile after you finish!', side: "left", align: 'start' }},
      { element: '#family-bio', popover: { title: 'Tell us about your family', description: 'Type whatever you want that best descripes your family', side: "bottom", align: 'start' }},
      { element: '#family-profile-photo', popover: { title: 'Add Profile Image', description: 'Click to change the profile image', side: "bottom", align: 'start' }},
      { element: '#family-cover-photo', popover: { title: 'Add Cover Image', description: 'Click to change the cover image', side: "bottom", align: 'start' }},
      { element: '#submit-button', popover: { title: 'Create Your Family', description: 'You may want to edit things later, You can do that in your family prfile', side: "bottom", align: 'start' }},
    ],
  });
  
  driverObj.drive();

