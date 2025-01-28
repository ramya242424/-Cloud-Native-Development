# Cloud-Native-Development - File Upload Web Application

This application allows users to upload image files, set their email addresses, and view their upload history. It integrates with Google Cloud Storage and Datastore to manage file uploads and metadata.

## Features
- **Email Registration**: Users can input their email addresses, which are stored in session to associate uploads with the email.
- **File Upload**: Users can upload image files (JPEG format). Each uploaded file is saved to the server and also uploaded to a Google Cloud Storage bucket.
- **Upload History**: Users can view a history of their previously uploaded files with clickable links to download them.
- **Logout**: Users can log out, which will clear their session.

## Tech Stack
- **Backend**: Flask
- **Cloud Storage**: Google Cloud Storage for storing files
- **Database**: Google Cloud Datastore for storing metadata about uploads (like filenames, URLs, and timestamps)
- **Frontend**: HTML5, CSS3, and Flask Jinja templating
