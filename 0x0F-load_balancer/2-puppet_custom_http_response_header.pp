node default {
  # Define the header name
  $header_name = 'X-Served-By'

  # Get the server hostname using the `fqdn` function
  $server_hostname = fqdn($name)

  # Include the nginx module (adjust if using a different module name)
  include nginx

  # Nginx server block configuration
  nginx::server {
    listen   80;
    server_name  $server_hostname;

    # ... other server block configuration options ...

    # Add the custom header directive
    location / {
      add_header $header_name  $server_hostname;
    }
  }
}
