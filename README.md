# brix
======
various scripts and code for brix

## proxy_update.py
------------------
make an api call to the proxy to update ip address

### todo: private-data
currently the proxy_url is being passed in as an arg. this should be set as
private data to make the jenkins setup more secure

### todo: verify-response
after making a call verify to ensure that the update is successful.

## ip_has_changed.py
----------------
find external ip and cache response. successfully exit if ip has changed
allowing for other jobs to run
