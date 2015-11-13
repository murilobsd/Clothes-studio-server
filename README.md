# Clothes-studio-client
Серверная часть для сайта "Lovingly"

### Run
<pre class="code">
    # apt-get install python3-pip
    # pip3 install > requirements.txt
    $ python3 app.py
</pre>

### Build docs
<pre class="code">
    $ hg clone https://bitbucket.org/birkenfeld/sphinx-contrib
    $ cd sphinx-contrib/httpdomain
    $ python setup.py build
    # python setup.py install
    $ cd docs
    $ make html
</pre>