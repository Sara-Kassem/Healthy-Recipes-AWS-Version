// ----------------------------------------//
// Show or hide the side bar upon clicking
// ----------------------------------------//
function openSideBar() {
    document.getElementById("sideNav").style.display = "block";
    }

function closeSideBar() {
    document.getElementById("sideNav").style.display = "none";
    }

// --------------------------------------------- //
// Hide flach message after a set amount of time //
// --------------------------------------------- //

flash = document.getElementById("flashMessages");

if (flash) {
    setTimeout(function() {
        flash.style.display = "none";
    }, 3000);
}

// --------------------------------------------------- //
// Display a preview for the new/modified recipe image //
// --------------------------------------------------- //

var imageInput = document.getElementById("uploadImage");

var imagePreview = document.getElementById("imagePreview");

if (imageInput) {

    imageInput.addEventListener('change', updateImageDisplay);

    var filePath = imageInput.value;
}

// allowed file types
var fileTypes = /(\.jpg|\.jpeg|\.png|\.gif)$/i;

// Check if the chosen file is valid 
function validFileType(file_path) {
    
    if(fileTypes.exec(filePath)){
        return true;
    } else {
        return false;
    }

}

// Display the selected images in the preview div
function updateImageDisplay() {

    // remove existing images
    while(imagePreview.firstChild) {
        imagePreview.removeChild(imagePreview.firstChild);
    }

    // get the selected image
    var curFile = imageInput.files;

    // append the image to document if chosen 
    if (curFile.length !== 0 && validFileType(filePath)) {

        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('imagePreview').innerHTML = '<img src="'+e.target.result+'"/>';
        };
        reader.readAsDataURL(imageInput.files[0]);
    }
}

// --------------------------------------------------- //
