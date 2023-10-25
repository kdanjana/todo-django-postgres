workers = 4              # Adjust the number of workers as needed
bind = "0.0.0.0:8000"    # The IP and port to bind to
timeout = 120            # Increase the timeout as needed for long-running requests
# Access log - records incoming HTTP requests
accesslog = "/var/log/gunicorn.access.log"
# Error log - records Gunicorn server goings-on
errorlog = "/var/log/gunicorn.error.log"
# Whether to send Django output to the error log 
capture_output = True
# How verbose the Gunicorn error logs should be 
loglevel = "info"