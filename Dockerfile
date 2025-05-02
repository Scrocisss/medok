FROM ubuntu:jammy

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y install \
        apache2 \
        libapache2-mod-php \
        libapache2-mod-auth-openidc \
        whatweb \
        php-bcmath \
        php-cli \
        php-curl \
        php-mbstring \
        php-gd \
        php-mysql \
        php-json \
        php-ldap \
        php-memcached \
        php-mime-type \
        php-pgsql \
        php-tidy \
        php-intl \
        php-xmlrpc \
        php-soap \
        php-uploadprogress \
        php-zip \
        libcap2-bin && \
    setcap 'cap_net_bind_service=+ep' /usr/sbin/apache2 && \
    dpkg --purge libcap2-bin && \
    apt-get -y autoremove && \
    a2disconf other-vhosts-access-log && \
    chown -Rh www-data. /var/run/apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    a2enmod rewrite headers expires ext_filter 

COPY src/000-default.conf /etc/apache2/sites-available
COPY src/mpm_prefork.conf /etc/apache2/mods-available
COPY src/status.conf      /etc/apache2/mods-available
COPY src/99-local.ini     /etc/php/7.4/apache2/conf.d
COPY src/ports.conf	  /etc/apache2/ports.conf

RUN chown -R www-data:www-data /var/www/html/ && \
    rm /var/www/html/index.html
    
COPY src/web/	/var/www/html/
EXPOSE 8000
USER root
ENTRYPOINT ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
