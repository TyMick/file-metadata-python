# Python file metadata microservice

This is a Python/[Flask](https://flask.palletsprojects.com/en/1.1.x/) port of my [Node.js file metadata microservice project](https://ty-file-metadata.glitch.me/), which was originally built to fulfill the following user stories:

1.  I can submit a form object that includes a file upload.
2.  The from file input field has the `name` attribute set to `"upfile"`. We rely on this in testing.
3.  When I submit something, I will receive the file name and size in bytes within the JSON response.
