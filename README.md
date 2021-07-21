# lampy-crud-app
A simple API running on a LAMPy stack. Code for a Python API (using FastAPI), and the configuration files for an Ubuntu-Apache web server.

## Requirements:
- Linux OS *(Ubuntu config provided, but I also successfully deployed this on an EC2 running Amazon Linux)*
- Apache
- MySQL
- Python 3, with pip and venv

## To use:
1. Clone the repository down on the server. *I used the default web server root, `/var/www/` for this, but the repo can go anywhere.*
2. __Web app setup:__ In the repo directory create a Python virtual environment *(`python -m venv <venv-name>`)*, and enable it *(`source <venv-name>/bin/activate`)*. Install the pip packages *(`pip install`)* listed in `requirements.txt`, and disable the venv *(`deactivate`)*.
3. __Apache setup:__ Copy the contents of `./apache2/sites-available/` to `/etc/apache2/sites-available/`, enable the site *(`a2ensite`)*, and restart Apache. *Apache is different on other distros but the config should work when placed in Apache's config directory with minor edits*
4. __Application server setup:__ Copy the contents of `./systemd/system/` to `/etc/systemd/system/`. Start
